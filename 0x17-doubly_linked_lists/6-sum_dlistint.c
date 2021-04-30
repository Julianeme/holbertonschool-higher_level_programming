#include "lists.h"

/**
 * sum_dlistint -  returns the number of elements in a doubly liked list
 * @head: a pointer to the element of the list
 * Return: the sum of the nodes
 */

int sum_dlistint(dlistint_t *head)
{
	int sum = 0;
	dlistint_t *temp = head;


	while (temp != NULL)
	{
		sum = sum + temp->n;
		temp = temp->next;
	}
return (sum);
}
