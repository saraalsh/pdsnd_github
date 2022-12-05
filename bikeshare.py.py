import time
import pandas as pd


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print()
    print("------------------------- welcome -------------------------".title())
    print()
    print('Let\'s explore some US bikeshare data!')

    # user input for city (chicago, new york city, washington).
    while True:
     city=input("Would you like to explore US bikeshare data for Chicago, New York, or Washington?\n")
     city=city.lower()
     if city in ["chicago", "new york", "washington"]: 
      break
     else:
         print()
         print("---- Invaild city input, please try again ----")
    print('_____________________________________________________')

    # user input for month (all, january, february, ... , june)
    while True:  
      month=input("Please enter which month ( January, February, ... , June), or 'all'.?\n")
      month=month.lower()
      if month in ['january', 'february', 'march', 'april', 'may', 'june','all']: 
        break
      else:
        print()
        print("---- Invaild month input, please try again ----")
    print('_____________________________________________________')

    # user input for day of week (all, monday, tuesday, ... sunday)
    while True:
     day=input("Please enter which day of week (Sunday, Monday,...etc) or 'all'?\n" )
     day=day.lower()
     if day in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday','all']: 
        break
     else:
         print()
         print("---- Invaild day input, please try again ---- ")
    print('_____________________________________________________') 

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # converts the Start Time column to datetime and creates new month and day of week columns
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filters by month if applicable and creates new dataframe
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    # filters by day of week if applicable and creates new dataframe
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\n The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df['month'].mode()[0]
    print('The Most Common Month:', common_month)

    # display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('The Most Common Day of The Week:', common_day)

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('The Most Common Starting Hour:', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\n The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start = df['Start Station'].mode()[0]
    print('Most commonly used start station:', common_start)

    # display most commonly used end station
    common_end = df['End Station'].mode()[0]
    print('Most commonly used end station:', common_end)

    # display most frequent combination of start station and end station trip
    df['Frequent Trip'] = df['Start Station'] + ' to ' + df['End Station']
    common_trip = df['Frequent Trip'].mode()[0]
    print('Most Frequent trip', common_trip) 

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating total and average trip duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time:', total_travel_time, 'seconds')

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Average travel time:', mean_travel_time, 'seconds')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating bikeshare User Stats\n')
    start_time = time.time()

    # Display counts of user types
    user_type_count = df['User Type'].value_counts()
    print('User Type Count:\n', user_type_count)

    # Display counts of gender
    try:
        gender_count = df['Gender'].value_counts()
        print('\nGender Count:\n', gender_count)
    except KeyError:
        print('\nGender Count: No data available.')

    # Display earliest, most recent, and most common year of birth
    try:
        birth_min = int(df['Birth Year'].min())
        print('\nEarliest year of birth:', birth_min)
    except KeyError:
        print('\nEarliest year of birth: No data available.')

    try:
        birth_max = int(df['Birth Year'].max())
        print('Most recent year of birth:', birth_max)
    except KeyError:
        print('Most recent year of birth: No data available.')

    try:
        birth_mode = int(df['Birth Year'].mode()[0])
        print('Most common year of birth:', birth_mode)
    except KeyError:
        print('Most common year of birth: No data available.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def view_all_details():
    
    view=input("do you want to view raw data for chicago, new york or washington? type yes or no: \n".title())
    view=view.lower()
    while view == 'yes':
        cities=input('''select which city :
                        A: Chicaho
                        B: New york
                        C: Washington \n'''.title())
        
        
        if cities.lower() == 'a':
         f=open("chicago.csv","r")
         data_display=f.read()
         print(data_display)
         f.close()
         print()
         break
        elif cities =='b':
         f=open("new_york.csv","r")
         data_display=f.read()
         print(data_display)
         f.close()
         print()
         break
        elif cities =='c':
         f=open("washington.csv","r")
         data_display=f.read()
         print(data_display)
         f.close()
         print()
         break
        else:
            print("Invaild selection, please try again".title())
            
    while view!='yes':
            break
   
            
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        view_all_details()

        restart = input('\nWould you like to restart and explore another city? please Enter yes or no.\n'.title())
        if restart.lower() != 'yes':
            print("----- see you next time -----".title())
            break


    
    
    
if __name__ == "__main__":
	main()