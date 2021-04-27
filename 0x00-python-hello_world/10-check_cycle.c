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
	listint_t *fast_ptr = NULL, *slow_ptr = NULL;

	*fast_ptr = *list;
	*slow_ptr = *list;

	if (!list || !list->next)
		return (0);
	while (fast_ptr && fast_ptr->next && slow_ptr)
	{
		fast_ptr = fast_ptr->next->next;
		slow_ptr = slow_ptr->next;
		if (fast_ptr == slow_ptr)
			return (1);
	}
	return (0);
}
