class TextProcessor:
    @staticmethod
    def clean_text(text):
        """
        Clean and preprocess text
        
        Args:
            text (str): Input text to clean
        
        Returns:
            str: Cleaned text
        """
        text = text.replace("\"", "")
        text = text.split("\\n")
        text = [line.replace("\'", "") for line in text if line != ""]
        return "\n ".join(text)