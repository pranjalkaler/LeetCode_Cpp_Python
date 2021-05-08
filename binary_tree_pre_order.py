class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        call_stack = []
        total = [ 0 ] * n
        last_operation = 0
        current_process_time = 0
        for x in logs:
            idx, operation, time = x.split(":")
            idx, time = int(idx), int(time)
            if operation == "start":
                if len(call_stack) == 0:
                    stack_val = [ idx, 0 ]
                else:
                    current_process_time = time - last_operation
                    call_stack[-1][1] += current_process_time
                    stack_val = [ idx, 0]
                last_operation = time
                call_stack.append(stack_val)
            elif operation == "end":
                stack_top = call_stack.pop()
                current_process_time = time - last_operation
                total[idx] += current_process_time
        return total                