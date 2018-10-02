# -*- coding: utf-8 -*-
# 车的数量是100
cars = 100
# 车的座位是 4.0
space_in_a_car = 4.0
# 乘客为90人
passengers = 90
# 司机为30人
drivers = 30
# 没有出行的汽车为汽车总数和司机的差值
cars_not_driven = cars - drivers
# 出行的汽车辆数为司机数
cars_driven = drivers

# 汽车容纳人数为出行车辆乘以车的座位
carpool_capacity = cars_driven * space_in_a_car
# 每辆车的平均乘客为乘客总数除以出行车辆
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available"
print "There are only", drivers, "drivers available"
print "There will be", cars_not_driven, "empty cars today"
print "We can transport", carpool_capacity, "people today"
print "We have", passengers, "to carpool today"
print "We need to put about", average_passengers_per_car, "in each car."
