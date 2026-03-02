from abc import ABC, abstractmethod

# 1. THE CONTRACT (The Interface)
# Any model we build MUST have a 'generate_audio' function.
class AudioModelInterface(ABC):
    @abstractmethod
    def generate_audio(self, text: str) -> str:
        pass

# 2. MOCK MODEL A
# Notice how it passes the interface inside the parentheses 
class QwenAudioModel(AudioModelInterface):
    def generate_audio(self, text: str) -> str:
        # Imagine 100 lines of complex Qwen AI code here
        return f"[Qwen AI V2] AUTOMATED DEPLOYMENT SUCCESS!. '{text}'"

# 3. MOCK MODEL B
class FutureFastModel(AudioModelInterface):
    def generate_audio(self, text: str) -> str:
        # Imagine 100 lines of a completely different AI's code here
        return f"[Future AI] Instantly generated voice for: '{text}'"