#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * listint_t *insert_node - inserts a number into a sorted linked list
 * @head: a double pointer to the head of the linked list
 * @number: number to be insterd
 * Return: a pointer to the new node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp = *head, *newnode = NULL;

	newnode = malloc(sizeof(listint_t));
	if (!newnode)
		return (NULL);
	newnode->n = number;
	if (*head == NULL)
	{
		newnode->next = NULL;
		*head = newnode;
		return (newnode);
	}
	if ((newnode->n) <= (temp->n))
	{
		newnode->next = *head;
		*head = newnode;
	}
	else
	{
		while (temp->next)
		{
			if ((newnode->n >= temp->n) && (newnode->n <= temp->next->n))
			{
				newnode->next = temp->next;
				temp->next = newnode;
				return (newnode);
			}
			temp = temp->next;
		}
		if (temp->next == NULL)
		{
			newnode->next = NULL;
			temp->next = newnode;
		}
	}
	return (newnode);
}
