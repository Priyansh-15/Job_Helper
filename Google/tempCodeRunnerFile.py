            google_experienced.append(job_data)
            
            wait.until(EC.element_to_be_clickable((By.XPATH,google_back_button))).click() 
            time.sleep(1.5)
            wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="search-results"]/li['+str(index-1)+']/div/a/div')))
            driver.execute_script("window.scrollTo(0, 1000)") 
            print("index")

        except TimeoutException:
            driver.quit()
            break

    add_to_csv(fieldnames,google_experienced,'Google_experienced_openings.csv')



def add_to_csv(fieldnames,google,title):
    with open(title, 'w', encoding='UTF8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writerows(google)


#Google_job_internship_scrape(1)