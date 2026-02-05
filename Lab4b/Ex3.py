# Name: Cassiddy Ginoza
# Date: Feb. 3, 2026

url = input("Enter a full URL: ")

cleaned_url = url.replace("http://", "").replace("https://", "").replace("www.", "")
#replace https:// with an empty string

print("Cleaned URL: ", cleaned_url)

parts = cleaned_url.split(".")
#split the cleaned URL into parts using the dot as a delimiter

domain = parts[1]
print("Domain: ", domain)

TLD = parts[2]

#We might get a trailing / character, so we need to remove it
#TLD_clean = TLD.strip("/")
TLD_clean = TLD.replace("/", "") #alternative way to clean TLD
print("Top-Level Domain: ", TLD_clean)