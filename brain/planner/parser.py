class CommandParser:

    def parse(self, text: str) -> list:
        # Simple rule-based parser (can be replaced by LLM-backed parser later)
        text_lower = text.lower().strip()
        parsed = []
        
        if "open github" in text_lower:
            parsed.append({
                "action": "open",
                "target": "github"
            })
            
        if "search" in text_lower:
            parts = text_lower.split("search")
            if len(parts) > 1:
                query = parts[1].strip()
                parsed.append({
                    "action": "search",
                    "target": query
                })
                
        return parsed
