from copy import deepcopy

actions = dict()
actions['Performing \'Open jar\''] = {
    "desirables": [
        "Jar opened",
        "Checking..."
    ],
    "undesirables": [
        {
            "event": "Jar spills",
            "unless": {
                "event": "Clean spills",
                "by": "end of cleanup"
            }
        }
    ],
    "termination": "Completed 'Open jar'"
}

open_actions = dict()
print()

with open('log') as f:
    lines = f.read().splitlines()
    for l in lines:
        for oa in open_actions.values():
            if l in oa['desirables']:
                oa['desirables'].remove(l)

            for u in oa['undesirables']:
                if l == u['event']:
                    print("Event '" + u['event'] + "' is undesirable but was found!")

            if l == oa['termination']:
                oa['completed'] = True

        # Register any new actions
        if l in actions.keys():
            open_actions[l] = deepcopy(actions[l])

print()
print()
print()
print(open_actions)
