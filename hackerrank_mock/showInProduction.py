import requests
import re

class showinproduction:

    def showsInProduction(self, startYear, endYear) -> list[str]:
        base_url = "https://jsonmock.hackerrank.com/api/tvseries"
        page = 1
        all_shows = []

        while True:
            response = requests.get(f"{base_url}?page={page}")
            data = response.json()
            shows = data['data']

            for show in shows:
                runtime = show.get("runtime_of_series", "")
                name = show.get("name", "")

                match = re.search(r'\((\d{4}(?:-\d{4})?)\)', runtime)
                if match:
                    runtime = match.group(1)
                if runtime.startswith("(") and ")" in runtime:
                    runtime = runtime[runtime.index("(") + 1: runtime.index(")")]

                if "-" in runtime:
                    start_str, end_str = runtime.split('-')
                elif "-" not in runtime:
                    start_str = end_str = runtime
                else:
                    continue
                try:
                    series_start = int(start_str.strip())
                except:
                    continue

                still_running = end_str.strip() == ""
                try:
                    series_end = int(end_str.strip()) if not still_running else None
                except:
                    series_end = None

                if series_start >= startYear:
                    if endYear == -1:
                        if still_running or series_end is None:
                            all_shows.append(name)
                    else:
                        if series_end is not None and series_end <= endYear:
                            all_shows.append(name)

            if page >= data['total_pages']:
                break
            page += 1

        return sorted(all_shows)