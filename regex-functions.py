#!/usr/bin/env python
import csv
import sys
import os
import re

# def check_web_address(text):
#   pattern = r"^[a-zA-Z0-9_\.\-\+]*\.[a-zA-Z]*$"
#   result = re.search(pattern, text)
#   return result != None
#
# print("check_web_address")
# print(check_web_address("gmail.com")) # True
# print(check_web_address("www@google")) # False
# print(check_web_address("www.Coursera.org")) # True
# print(check_web_address("web-address.com/homepage")) # False
# print(check_web_address("My_Favorite-Blog.US")) # True
#
#
# def contains_acronym(text):
#   pattern = r"\([A-Z1-9][a-zA-Z1-9]*\)"
#   result = re.search(pattern, text)
#   return result != None
#
# print("contains_acronym")
# print(contains_acronym("Instant messaging (IM) is a set of communication technologies used for text-based communication")) # True
# print(contains_acronym("American Standard Code for Information Interchange (ASCII) is a character encoding standard for electronic communication")) # True
# print(contains_acronym("Please do NOT enter without permission!")) # False
# print(contains_acronym("PostScript is a fourth-generation programming language (4GL)")) # True
# print(contains_acronym("Have fun using a self-contained underwater breathing apparatus (Scuba)!")) # True
#
#
# def check_zip_code(text):
#   result = re.search(r" +[0-9]+[0-9]+[0-9]+[0-9]+[0-9]+", text)
#   return result != None
#
# print("check_zip_code")
# print(check_zip_code("The zip codes for New York are 10001 thru 11104.")) # True
# print(check_zip_code("90210 is a TV show")) # False
# print(check_zip_code("Their address is: 123 Main Street, Anytown, AZ 85258-0001.")) # True
# print(check_zip_code("The Parliament of Canada is at 111 Wellington St, Ottawa, ON K1A0A9.")) # False
#
#
#
# def check_time(text):
#   pattern = r"^[1-9][0-2]?:[0-5][0-9] ?[AM|PM|am|pm]"
#   result = re.search(pattern, text)
#   return result != None
#
# print("check_time")
# print(check_time("12:45pm")) # True
# print(check_time("9:59 AM")) # True
# print(check_time("6:60am")) # False
# print(check_time("five o'clock")) # False
#
#
# def rearrange_name(name):
#   result = re.search(r"^([\w \.-]*),([\w \.-]*)$", name)
#   if result == None:
#     return name
#   return "{} {}".format(result[2], result[1])
#
# print("rearrange_name")
# name=rearrange_name("Kennedy, John F.")
# print(name)
#
#
# def long_words(text):
#   pattern = r"\b[a-zA-Z]{7,}\b"
#   result = re.findall(pattern, text)
#   return result
#
# print("at least 7 characters long")
# print(long_words("I like to drink coffee in the morning.")) # ['morning']
# print(long_words("I also have a taste for hot chocolate in the afternoon.")) # ['chocolate', 'afternoon']
# print(long_words("I never drink tea late at night.")) # []
#
#
# def extract_pid(log_line):
#     regex = r"\[(\d+)\]\: (\b[A-Z]+\b)"
#     result = re.search(regex, log_line)
#     if result is None:
#         return None
#     return "{} ({})".format(result[1],result[2])
#
# print(extract_pid("July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade")) # 12345 (ERROR)
# print(extract_pid("99 elephants in a [cage]")) # None
# print(extract_pid("A string that also has numbers [34567] but no uppercase message")) # None
# print(extract_pid("July 31 08:08:08 mycomputer new_process[67890]: RUNNING Performing backup")) # 67890 (RUNNING)
#
#
#
# def transform_record(record):
#   new_record = re.sub(r"\b(\d{3}-\d{3}-?\d{4})\b",r"+1-\1",record)
#   return new_record
#
# print(transform_record("Sabrina Green,802-867-5309,System Administrator"))
# # Sabrina Green,+1-802-867-5309,System Administrator
#
# print(transform_record("Eli Jones,684-3481127,IT specialist"))
# # Eli Jones,+1-684-3481127,IT specialist
#
# print(transform_record("Melody Daniels,846-687-7436,Programmer"))
# # Melody Daniels,+1-846-687-7436,Programmer
#
# print(transform_record("Charlie Rivera,698-746-3357,Web Developer"))
# # Charlie Rivera,+1-698-746-3357,Web Developer
#
#
# def multi_vowel_words(text):
#   pattern = r"\b\w*[aeiou]{3}[^aeiou\s]*\w*\b"
#   result = re.findall(pattern, text)
#   return result
#
# print(multi_vowel_words("Life is beautiful"))
# # ['beautiful']
#
# print(multi_vowel_words("Obviously, the queen is courageous and gracious."))
# # ['Obviously', 'queen', 'courageous', 'gracious']
#
# print(multi_vowel_words("The rambunctious children had to sit quietly and await their delicious dinner."))
# # ['rambunctious', 'quietly', 'delicious']
#
# print(multi_vowel_words("The order of a data queue is First In First Out (FIFO)"))
# # ['queue']
#
# print(multi_vowel_words("Hello world!"))
#
#
#
#
#
# def transform_comments(line_of_code):
#   result = re.sub("([\#]{1,})", "//", line_of_code)
#   return result
#
# print(transform_comments("### Start of program"))
# # Should be "// Start of program"
# print(transform_comments("  number = 0   ## Initialize the variable"))
# # Should be "  number = 0   // Initialize the variable"
# print(transform_comments("  number += 1   # Increment the variable"))
# # Should be "  number += 1   // Increment the variable"
# print(transform_comments("  return(number)"))
# # Should be "  return(number)"
#
#
# def convert_phone_number(phone):
#   result = re.sub(r"\b(\d{3})-(\d{3})-(\d{4}\b)", r"(\1) \2-\3", phone)
#   return result
#
# print(convert_phone_number("My number is 212-345-9999.")) # My number is (212) 345-9999.
# print(convert_phone_number("Please call 888-555-1234")) # Please call (888) 555-1234
# print(convert_phone_number("123-123-12345")) # 123-123-12345
# print(convert_phone_number("Phone number of Buckingham Palace is +44 303 123 7300")) # Phone number of Buckingham Palace is +44 303 123 7300
#
#
#
#
# def contains_domain(address, domain):
#   """Returns True if the email address contains the given,domain,in the domain position, false if not."""
#   domain = r'[\w\.-]+@'+domain+'$'
#   if re.match(domain,address):
#     return True
#   return False
#
#
# def replace_domain(address, old_domain, new_domain):
#   """Replaces the old domain with the new domain in the received address."""
#   old_domain_pattern = r'' + old_domain + '$'
#   address = re.sub(old_domain_pattern, new_domain, address)
#   return address
#
# def main():
#   """Processes the list of emails, replacing any instances of the old domain with the new domain."""
#   old_domain, new_domain = '', ''
#   csv_file_location = '/home/student-02-cdf5c0abcb20/data/user_emails.csv'
#   report_file = '/home/student-02-cdf5c0abcb20/data' + '/updated_user_emails.csv'
#   user_email_list = []
#   old_domain_email_list = []
#   new_domain_email_list = []
#
#   with open(csv_file_location, 'r') as f:
#     user_data_list = list(csv.reader(f))
#     user_email_list = [data[1].strip() for data in user_data_list[1:]]
#
#     for email_address in user_email_list:
#       if contains_domain(email_address, old_domain):
#         old_domain_email_list.append(email_address)
#         replaced_email = replace_domain(email_address,old_domain,new_domain)
#         new_domain_email_list.append(replaced_email)
#
#     email_key = ' ' + 'Email Address'
#     email_index = user_data_list[0].index(email_key)
#
#     for user in user_data_list[1:]:
#       for old_domain, new_domain in zip(old_domain_email_list, new_domain_email_list):
#         if user[email_index] == ' ' + old_domain:
#           user[email_index] = ' ' + new_domain
#   f.close()
#
#   with open(report_file, 'w+') as output_file:
#     writer = csv.writer(output_file)
#     writer.writerows(user_data_list)
#     output_file.close()
#
# main()
#
#
#
# logfile = sys.argv[1]
# with open(logfile) as f:
#   for line in f:
#     if "CRON" not in line:
#         continue
#     pattern = r"USER \((\w+)\)$"
#     result = re.search(pattern, line)
#     print(result[1])
#
#
#
#
# def show_time_of_pid(line):
#   pattern = r"(\w\w\w \d\d? \d\d:\d\d:\d\d).*\[(\d{5})\]"
#   result = re.search(pattern, line)
#   return result[1] + " pid:" + result [2]


log_file = "C:/Users/User/Desktop/fishy.log"


def error_search(log_file):
	error = input("What is the error? ")
	returned_errors = []

	with open(log_file, mode='r', encoding='UTF-8') as file:
		for log in file.readlines():
			error_patterns = ["error"]
			for i in range(len(error.split(' '))):
				error_patterns.append(r"{}".format(error.split(' ')[i].lower()))

			if all(re.search(error_pattern, log.lower()) for error_pattern in error_patterns):
				returned_errors.append(log)
			file.close()
		return returned_errors


def file_output(returned_errors):
	with open(os.path.expanduser('~') + '/data/errors_found.log', 'w') as file:
		for error in returned_errors:
			file.write(error)
		file.close()


if __name__ == "__main__":
	log_file = sys.argv[1]
	returned_errors = error_search(log_file)
	file_output(returned_errors)
	sys.exit(0)
