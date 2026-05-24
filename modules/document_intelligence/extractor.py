
import os
import json
import logging
import requests
import re
from typing import Dict, Any, Optional

logger = logging.getLogger(__name__)

# Set logging level for this module
logging.basicConfig(level=logging.INFO)



from ..llm_gateway import LLMGateway

logger = logging.getLogger(__name__)

class OllamaFinancialExtractor:
    """
    Handles financial extraction with high-reliability cascading fallback.
    """
    
    def __init__(self, **kwargs):
        self.gateway = LLMGateway()

    def _call_llm(self, prompt: str, require_json: bool = True) -> str:
        """Calls the centralized LLM gateway."""
        return self.gateway.ask(prompt, require_json=require_json)





    def extract_financials(self, text: str) -> Dict[str, Any]:
        """
        Takes raw text and returns a dictionary of financial metrics.
        """
        # Optimized context for speed & local LLM reliability
        context = text[:35000]


        prompt = f"""
        Extract the following Indian corporate financial metrics from the provided text.
        IMPORTANT: Use CONSOLIDATED figures. If Crore/Lakh isn't specified, assume Rupees in Crores.
        Return EXCLUSIVELY a JSON object. For currency, convert all values to CRORES.
        
        Required Fields:
        - company_name (String)
        - revenue_cr (Float)
        - ebitda_cr (Float)
        - net_profit_cr (Float)
        - total_assets_cr (Float)
        - total_liabilities_cr (Float)
        - current_ratio (Float)
        - debt_to_equity (Float)
        - interest_coverage (Float)
        
        Text:
        {context}
        
        JSON Response:
        """
        

        print(f"DEBUG: Starting financial extraction for {len(context)} chars of text...")
        raw_response = self._call_llm(prompt)
        print(f"DEBUG: Received financial response.")

        
        try:
            # Clean response if LLM added markdown
            clean_json = re.sub(r'```json|```', '', raw_response).strip()
            data = json.loads(clean_json)
            
            # Robustness: Ensure data is a dictionary
            if not isinstance(data, dict):
                logger.error(f"LLM returned non-dictionary response: {type(data)}")
                data = {}
            
            # Basic normalization (ensure all keys exist)
            defaults = {
                "company_name": "Unknown",
                "revenue_cr": 0.0,
                "ebitda_cr": 0.0,
                "net_profit_cr": 0.0,
                "total_assets_cr": 0.0,
                "total_liabilities_cr": 0.0,
                "current_ratio": 0.0,
                "debt_to_equity": 0.0,
                "interest_coverage": 0.0
            }
            defaults.update(data)
            return defaults
            
        except Exception as e:
            logger.error(f"Failed to parse LLM response: {raw_response}")
            return {}


    def extract_multi_year(self, text: str) -> Dict[str, Any]:
        """
        Extracts financial metrics for the current and previous financial year.
        """
        # Optimized context
        context = text[:30000]
        prompt = f"""
        Extract consolidated financial metrics for the LAST TWO financial years.
        Return EXCLUSIVELY a JSON object with 'current_year' and 'previous_year' keys.
        Each should contain: revenue_cr, net_profit_cr, total_assets_cr.
        
        Text:
        {context}
        
        JSON Response:
        """
        raw_response = self._call_llm(prompt)
        try:
            clean_json = re.sub(r'```json|```', '', raw_response).strip()
            data = json.loads(clean_json)
            return data if isinstance(data, dict) else {"current_year": {}, "previous_year": {}}
        except:
            return {"current_year": {}, "previous_year": {}}


    def extract_risks(self, text: str) -> list:
        """Extracts qualitative risks from the text."""
        # Optimized context
        context = text[:25000]
        prompt = f"""
        Analyze the following text and identify 3 potential credit risks.
        Return EXCLUSIVELY a JSON list of objects with 'category', 'risk', and 'impact' (Low/Medium/High).
        
        Text:
        {context}
        
        JSON Response:
        """
        raw_response = self._call_llm(prompt)
        try:
            clean_json = re.sub(r'```json|```', '', raw_response).strip()
            data = json.loads(clean_json)
            return data if isinstance(data, list) else []
        except:
            return []



