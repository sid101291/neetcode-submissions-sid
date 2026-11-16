class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        master_scoreboard = {}
        window_size = len(s1)
        current_window = {}
        left = 0

        for c in s1:
            master_scoreboard[c] = master_scoreboard.get(c,0) + 1

        for right in range(len(s2)):

            char_in  = s2[right]

            current_window[char_in] = current_window.get(char_in,0) + 1

            if right - left + 1 > window_size:

                char_out = s2[left]

                current_window[char_out] -= 1

                if current_window[char_out] == 0:
                    del current_window[char_out]

                left += 1

            if right - left + 1 == window_size:

                if current_window == master_scoreboard:

                    return True

        return False




            