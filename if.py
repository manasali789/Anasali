alien_0={'x__position':0,'y_position':25,'speed':'medium'}

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
alien_0['x__position'] =alien_0['x__position']+x_increment
print(alien_0)  

