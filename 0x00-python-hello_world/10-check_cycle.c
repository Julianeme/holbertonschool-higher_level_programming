#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - checks if there is a cycle in a singly linked list
 * @list: singly linked list to be checked
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *fast_ptr, *slow_ptr;

	fast_ptr = list->next;
	slow_ptr = list;

	if (!list || list->next)
		return (0);

	while (fast_ptr && slow_ptr)
	{
		if ((fast_ptr == slow_ptr) &&)
			return(1)
		fast_ptr = fast_ptr->next->next;
		slow_ptr = slow_ptr->next;
	}
	return (0);
}
