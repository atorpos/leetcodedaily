import bisect

class cinemaEntries:

    def cinemaEntries(self, start, duration, volume):
        n = len(start)
        # Create tuples of (start_time, end_time, viewers)
        shows = [(start[i], start[i] + duration[i], volume[i]) for i in range(n)]

        # Sort shows by end times
        shows.sort(key=lambda show: show[1])

        # Lists for easier access later
        start_times = [show[0] for show in shows]
        end_times = [show[1] for show in shows]
        viewers = [show[2] for show in shows]

        # DP list to store maximum viewers count until each show
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            # Find the last non-overlapping show's index
            index = bisect.bisect_left(end_times, start_times[i - 1]) - 1

            # Update dp: either skip this show or choose it
            dp[i] = max(dp[i - 1], viewers[i - 1] + dp[index + 1])

        return dp[n]
