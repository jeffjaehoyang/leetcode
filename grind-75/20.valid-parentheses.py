class Solution:
    def isValid(self, s: str) -> bool:
        matching_bracket = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        stack = []
        for p in s:
            if p in matching_bracket:
                stack.append(p)
            elif len(stack) == 0:
                return False
            else:
                last_opening_bracket = stack.pop()
                target_closing_bracket = matching_bracket[last_opening_bracket]
                if target_closing_bracket != p:
                    return False
        return len(stack) == 0
