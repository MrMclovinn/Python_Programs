### 11 / 22 / 2020
### Author: Elijah Oleary
### Using the pop() method

subscribers = ['tony@example.com', 'john@example.com', 'mary@example.com']
print(subscribers)

popped_subscriber = subscribers.pop()

print(subscribers)

print(popped_subscriber)

subscribers = ['tony@example.com', 'john@example.com', 'mary@example.com']
first_subscriber = subscribers.pop(0)

print("Your first subscriber was " + first_subscriber + ".")

subscribers = ['tony@example.com', 'john@example.com', 'mary@example.com']
print(subscribers)

subscribers.remove('john@example.com')

print(subscribers)

subscribers = ['tony@example.com', 'john@example.com', 'mary@example.com']
subscribed_by_mistake = 'tony@example.com'
subscribers.remove(subscribed_by_mistake)

print(subscribers)

print("\nThis person " + subscribed_by_mistake + " did not mean to sign up")