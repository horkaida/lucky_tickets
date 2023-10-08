from threading import Thread

def generate_tickets(tickets_number, digits_in_ticket):
    return [f"%.{digits_in_ticket}d" % i for i in range(tickets_number)]

def get_ticket_groups(tickets):
    return [tickets[x:x + len(tickets) // 4] for x in range(0, len(tickets), len(tickets) // 4)]

def get_lucky_ticket(group):
    for i in group:
        i = list(map(int, i))
        if i[0]+i[1]+i[2]==i[3]+i[4]+i[5]:
            lucky_tickets.append(i)

if __name__ == '__main__':
    lucky_tickets = []
    tickets = generate_tickets(1000000, 6)
    ticket_groups = get_ticket_groups(tickets)
    threads = []
    for group in ticket_groups:
        threads.append(Thread(target=get_lucky_ticket, args=[group]))
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print(len(lucky_tickets))
