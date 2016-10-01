# http://stackoverflow.com/questions/39785203/ruby-if-boolean-true-return-first-name-from-same-row-csv/39786166#39786166

# require 'csv'

# def customer_check(user_pin)

  # x = false
  # puts x
  # CSV.read('customers.csv', headers: true).any? do |row|
    # x = true if row['customerNo'] == user_pin and row['lastName'] == "Dunbar"
    # yellow = row['firstName']
    # puts row['customerNo']
    # puts row['lastName']
    # puts x
  # puts x
  # if x == true then
    # puts "Welcome back #{yellow}."
    # sleep(1.5)
  # else
    # puts "login failed. Please try again in 3 seconds..."
    # sleep(3.0)
    # # login_start
  # end
    # # navigation_menu
# end
# end

# customer_check('1')

require 'csv'

def customer_check(user_pin)

  x = false

  CSV.read('customers.csv', headers: true).any? do |row|
    x = true if row['customerNo'] == user_pin && row['lastName'] == "Dunbar"
    yellow = row['firstName']
  # The if/else clauses need to be indented within the CSV.read
    if x                                           # <-- "== true" is redundant
      # puts "Welcome back #{yellow}."             # you can lose "yellow" if you want to
      puts "Welcome back #{row['firstName']}."
      sleep(1.5)
      # return yellow                              # <-- RETURN VALUE
      return row['firstName']                      # <-- RETURN VALUE
    else  
      puts "login failed. Please try again in 3 seconds..."
      sleep(3.0)
      # login_start
    end
  # navigation_menu

  end

end

return_name = customer_check('1')                  # <-- "Welcome back John"
puts return_name                                   # <-- "John" is the RETURN VALUE



