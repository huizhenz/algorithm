secret_code, meeting_point, time = input().split()
time = int(time)

# Please write your code here.
class Meeting:
    def __init__(self, code, point, time):
        self.code = code
        self.point = point
        self.time = time

meeting = Meeting(secret_code, meeting_point, time)
print("secret code :", meeting.code)
print("meeting point :", meeting.point)
print("time :", meeting.time)