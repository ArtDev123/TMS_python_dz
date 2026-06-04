from typing import Optional


class Soda:
    def __init__(self, flavor: Optional[str] = None) -> None:
        self.flavor: Optional[str] = flavor

    def __str__(self) -> str:
        if self.flavor:
            return f"У вас газировка с {self.flavor} вкусом"
        return "У вас обычная газировка"
