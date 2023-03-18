#include "lists.h"



int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	while (slow && fast && fast->next) {
		slow = slow->next;
		fast = fast->next->next;
        /* If fast pointer catches up with slow pointer, there is a cycle */
		if (slow == fast) {
			return 1;
		}
	}
	/* If there is no cycle, return 0 */
	return 0;
}
