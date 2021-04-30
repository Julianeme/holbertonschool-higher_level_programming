#include "lists.h"

/**
 * add_dnodeint - adds a node at the beggining of a linked list
 * @head: a double pointer to the head of the linked list
 * @n: the data of the new node
 * Return: the address of the new element, or NULL if it failed
 */

dlistint_t *add_dnodeint(dlistint_t **head, const int n)
{
	dlistint_t *new = NULL, *temp = *head;

	new = malloc(sizeof(dlistint_t));
	if (!new)
		return (NULL);
	new->n = n;
	if (*head == NULL)
	{
		new->prev = NULL;
		new->next = *head;
		*head = new;
	}
	else
	{
		new->prev = NULL;
		new->next = *head;
		temp->prev = new;
		*head = new;
	}
	return (*head);
}
