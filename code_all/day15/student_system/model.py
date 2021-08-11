class StudentModel:
    """
        学生模型：封装数据
    """

    def __init__(self, name="", age=0, score=0, sid=0):
        self.name = name
        self.age = age
        self.score = score
        self.sid = sid  # 学生全球唯一标识符

    def __str__(self):
        return f"{self.name}的编号是{self.sid},年龄是{self.age},成绩是{self.score}"

    # 相同依据
    def __eq__(self, other):
        return self.sid == other