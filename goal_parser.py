class Solution:
    def interpret(self, command: str) -> str:
        command = command.replace("()", "o", command.count("()"))
        command = command.replace("(al)", "al", command.count("(al)"))
        return command