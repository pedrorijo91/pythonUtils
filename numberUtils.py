import math

def is_prime(n):
    if n < 0:
        return False
    for j in range(2, int(math.sqrt(n)) + 1):
        if n%j == 0:
            return False
    return True

def divisors(n):
        count = 1
        divisors = []
        for i in range(1, int(math.sqrt(n)) + 1):
                if n % i == 0:
                        divisors.append(i)
                        divisors.append(n/i)
        divisors = list(set(divisors))
        return sorted(divisors)

def combinations(n,r):
        return math.factorial(n) / (math.factorial(r) * math.factorial(n-r))

def number_3d_to_text(n):
        dictionary = {
        1: 'one', 
        2: 'two', 
        3: 'three', 
        4: 'four', 
        5: 'five', 
        6: 'six', 
        7: 'seven', 
        8: 'eight', 
        9: 'nine', 
        10: 'ten', 
        11: 'eleven', 
        12: 'twelve', 
        13: 'thirteen', 
        14: 'fourteen', 
        15: 'fifteen', 
        16: 'sixteen', 
        17: 'seventeen', 
        18: 'eighteen', 
        19: 'nineteen', 
        20: 'twenty', 
        30: 'thirty',
        40: 'forty',
        50: 'fifty',
        60: 'sixty',
        70: 'seventy', 
        80: 'eighty',
        90: 'ninety'
	}   

	word = ""

	if n >= 100:
		word += dictionary[n / 100] + " hundred"
		n = n % 100	
		
		if n <> 0:
			word += " and" 
	if n > 20:
		if len(word) > 0:
			word += " "
		word += dictionary[(n / 10) * 10]
		n = n % 10

	if n <= 20 and n > 0:
		if len(word) > 0:
			word += " "
		word += dictionary[n]

	return word

def number_to_text(n):
#http://www.calculator.org/calculate-online/mathematics/text-number.aspx 
	
	thousands = ""
	units = ""
	word = ""

	if n > 999999:
		print "ERROR: Maximum value of 999999. You inserted", n
		return ""
	
	if n >= 1000:
		thousands = number_3d_to_text(n/1000) + " thousand"
		n = n % 1000

	units = number_3d_to_text(n)

	if len(thousands) > 0:
		word += thousands 
	
	if len(units) > 0 and len(word) > 0:
		word += " "
	
	word += units

	return word


