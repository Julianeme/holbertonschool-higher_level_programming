#include "lists.h"

/**
 * free_dlistint -  frees the memory allocated for a doubly linked list
 * @head: a pointer to start of the element of the list
 */

void free_dlistint(dlistint_t *head)
{
	dlistint_t *temp = NULL;

	while (head)
	{
		temp = head->next;
		free(head);
		head = temp;
	}
}
