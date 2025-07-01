from .base_provider import JokeProvider

class TinJokeProvider(JokeProvider):
    """Cung cấp các câu truyện cười của Anh Tín."""

    def get_jokes(self) -> list[str]:
        return [
            "Anh Tín nói: 'Tại sao con cá lại bơi nhanh? Vì nó có vây (Vậy) đó.'",
            "Anh Tín đố: 'Cái gì mà đi thì nằm, đứng cũng nằm, nhưng nằm lại đứng? Bàn chân đó.'",
            "Anh Tín lại đùa: 'Anh không thích nói đùa, anh chỉ thích nói thật... là anh đang đùa.'"
        ]