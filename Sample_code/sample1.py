import pickle


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.area = width * height


rect = Rectangle(10, 20)

# 사각형 rect 객체를 직렬화 (Serialization)
with open('rect.data', 'wb') as f:
    pickle.dump(rect, f)


# 역직렬화 (Deserialization)
with open('rect.data', 'rb') as f:
    r = pickle.load(f)

print("%d x %d" % (r.width, r.height))
