import time
import locale

def format_ft_time():
	locale.setlocale(locale.LC_ALL, 'en_US.utf8')
	seconds = time.time()
	format_seconds = locale.format_string("%.4f", seconds, grouping=True)

	print(f"Seconds since January 1, 1970: {format_seconds} or {seconds:.2e} in decimal notation")
	
	print(time.strftime("%b %d %Y"))

	

def main():
	format_ft_time()

if __name__ == "__main__":
	main()