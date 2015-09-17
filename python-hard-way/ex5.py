name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 #lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print 'Let\'s talk about %s.' % name
print 'He\'s %d inches tall.' % height
print 'He\'s %f centimeters tall.' % (height * 2.54)
print 'He\'s %d pounds heavy.' % weight
print 'He\'s %f kilograms heavy.' % (weight * 0.453592)
print 'He\'s got %s and %s hair.' % (eyes, hair)
print 'His teeth are usually %s depending on the coffee.' % teeth

print 'If I add %d, %d, and %d, I get %d.' % (age, height, weight,
        age + weight + height)

print 'This is a thing: %r' % 2.5541234e4
