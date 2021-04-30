#include "lists.h"

/**
 * add_dnodeint_end - adds a node at the end of a doubly linked list
 * @head: a double pointer to the head of the linked list
 * @n: the data of the new node
 * Return: the address of the new element, or NULL if it failed
 */

dlistint_t *add_dnodeint_end(dlistint_t **head, const int n)
{
	dlistint_t *new = NULL, *temp = *head;

	new = malloc(sizeof(dlistint_t));
	if (!new)
		return (NULL);
	new->n = n;
	if (*head == NULL)
	{
		new->n = n;
		new->prev = NULL;
		new->next = *head;
		*head = new;
	}
	else
	{
		while (temp->next)
			temp = temp->next;
		new->next = NULL;
		new->prev = temp;
		temp->next = new;
	}
	return (*head);
}
