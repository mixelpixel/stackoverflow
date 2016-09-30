# http://stackoverflow.com/questions/39785203/ruby-if-boolean-true-return-first-name-from-same-row-csv/39786166#39786166

require 'csv'

CSV.read('customers.csv', headers: true).any? do |row|
    x = true if row['customerNo'] == '1' and row['lastName'] == "Dunbar"
    yellow = row['firstName']

    if x == true
        puts "Welcome back #{yellow}."
        sleep(1.5)
    else
        puts "login failed. Please try again in 3 seconds..."
        sleep(3.0)
    end
end