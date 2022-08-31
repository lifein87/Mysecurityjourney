from googlesearch import search
import pyfiglet

ascii_banner = pyfiglet.figlet_format("THREAT FINDER")
print(ascii_banner)
print("_" * 50)
print("Searching the web...")
print("_" * 50)


results = search("latest vulnerabilities cybersecurity threats cybersecurity attack patches new malware attack", num=5, lang="en", tld="com", stop=5)



results = list(results)

print(results)