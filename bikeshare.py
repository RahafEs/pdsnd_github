import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicagocity': 'chicagocity.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:

        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid input city=input(" Would you like to see data for Chicago , New York , Washington?")

    city=input("Would you like to see data for Chicago , New York City, or Washington? ").lower()

    while city not in CITY_DATA:
        print("your city not found plaese try again ")
        city=input("Would you like to see data for Chicago , New York City, or Washington? ").lower()


# TO DO: get user input for month (all, january, february, ... , june)
    month=int(input("Which month? Please type your response as an integer "))


 # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day=int(input("Which day? Please type your response as an integer "))

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
    df=pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.dayofweek

    df = df[df['month']==month]
    df = df[df['day']==day]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month=df["month"].mode()[0]
    print("Most common month is ",common_month)



    # TO DO: display the most common day of week
    common_day=df["day"].mode()[0]
    print("Most common day is" ,common_day)




    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_Start_hour=df["hour"].mode()[0]
    print("Most common Start hour is" ,common_Start_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station=df["Start Station"].mode()[0]
    print("Most common start station is ", common_start_station)


    # TO DO: display most commonly used end station
    common_end_station=df["End Station"].mode()[0]
    print("Most common end station is ", common_end_station)


    # TO DO: display most frequent combination of start station and end station trip
    common_trip_duration=(df["Start Station"] + " - " + df["End Station"]).mode()[0]
    print("Most common trip duration is ", common_trip_duration)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time=df["Trip Duration"].sum()
    print("total travel time" ,total_time )

    # TO DO: display mean travel time
    mean_time=df["Trip Duration"].mean()
    print("mean travel time", mean_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    if "Gender" in df:
        # TO DO: Display counts of gender
        Gender = df["Gender"].value_counts()
        print(Gender)

        # TO DO: Display earliest, most recent, and most common year of birth
        print("The earliest year of birth :" ,df["Birth Year"].min())
        print("The most recent year of birth :",df["Birth Year"].max())
        print("The most common year of birth :",df["Birth Year"].mode()[0])
    else:
        print("Gender and birth year dosn't exist")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        num=0
        while True :
            data=input("do you want display data ? enter yes or no ")
            if data == "no":
                break
            else:
                print(df.iloc[num:num+5])
                num+=5

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
