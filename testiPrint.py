import re

log_file = 'C:\esimerkki\pyyttonRojekti\data3.log'  # Log tiedoston sijainti
start_time = "07:00"  # alkuaika
end_time = "15:30"    # Loppuaika
output_log_file = 'C:\esimerkki\pyyttonRojekti\loppusijoituspaikka.log'  # Tähän se mihin tiedostoon haluut sen


prev_second = None


with open(output_log_file, 'w') as output_file:
    
    try:
        with open(log_file, 'r') as file:
            for line in file:
                
                split_line = line.strip().split('\t')
                
                # Extract timestamp from the split line
                timestamp = split_line[0]
                # Extract the time part (HH:MM:SS) from the timestamp
                time_part = timestamp.split()[1].split('.')[0]
                current_second = time_part.split(':')[-1]  # Extract the second
                
                
                if start_time <= time_part <= end_time:
                    
                    if current_second != prev_second:
                        cleaned_line = re.sub(r'<..>', '', line)  
                        output_file.write(cleaned_line.strip() + '\n')  
                        prev_second = current_second  
    except FileNotFoundError:
        print(f"eI LÖYDY'{log_file}' ")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

print(f"Filtteröidyt rivit printattu tiedostoon '{output_log_file}'. :D")
