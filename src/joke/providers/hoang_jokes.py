from .base_provider import JokeProvider

class HoangJokeProvider(JokeProvider):
    """Cung cấp các câu truyện cười của Anh Hoàng."""

    def get_jokes(self) -> list[str]:
        return [
            "Anh Hoàng đùa rằng: 'Code của anh không có bug, chỉ có những tính năng không mong đợi.'",
            "Anh Hoàng kể: 'Hôm qua anh debug 10 tiếng, hóa ra quên cắm điện màn hình.'",
            "Một câu đùa khác của Anh Hoàng: 'Deadline cũng giống như crush, càng đến gần càng thấy áp lực.'"
        ]