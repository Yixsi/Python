def reto_3(dictionary: dict) -> str:
    if dictionary:
        dictionary = tutores
        values = dictionary.values()
        major = max(values)
        keys = [key for key in dictionary if dictionary[key] == major]
        return ', '.join(keys)
    else:
        return None

tutores = {'John': 16, 'Alex': 12, 'Bob': 8, 'Mike': 14, 'Molly': 14}
tutor = reto_3(tutores)
print("Best: {}".format(tutor))

tutores = {'John': 12, 'Bob': 14, 'Mike': 16, 'Molly': 16, 'Adam': 10}
tutor = reto_3(tutores)
print("Best: {}".format(tutor))

tutores = None
tutor = reto_3(tutores)
print("Best: {}".format(tutor))

