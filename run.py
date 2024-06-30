from booking.booking import Booking

with Booking(teardown=False) as bot:
    bot.land_First_Page()
    bot.dismiss_Offer()
    bot.change_currency()
    input("wait")