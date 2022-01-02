# Class that converts a version string to a sortable object.
# Problem only requires sorting, so all comparison methods other
# than __lt__ are irrelevant
class VersionNumber:
    def __init__(self, str):
        self.version = map(int, str.split("."))

    def __lt__(self, other):
        if not isinstance(other, VersionNumber):
            return NotImplemented

        for i in range(len(self.version)):
            # self has more version integers, must be sorted after other
            if i >= len(other.version):
                return False
            # compare current version integer and return appropriately if they differ
            if self.version[i] < other.version[i]:
                return True
            if self.version[i] > other.version[i]:
                return False
        # self has less version integers, must be less than
        return True

    def __str__(self):
        return ".".join(map(str, self.version))


def solution(l):
    l.sort(key=VersionNumber)
    return l
