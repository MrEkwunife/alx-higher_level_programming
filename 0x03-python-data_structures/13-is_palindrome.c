#include "lists.h"

/**
* listint_reversed_ - This fun reverses a linked list
* @head: pointer to the head node in the list
* Return: pointer head node in the new list
*/
void listint_reversed_(listint_t **head)
{
	listint_t *prv = NULL;
	listint_t *curr = *head;
	listint_t *next = NULL;

	while (curr)
	{
		next = curr->next;
		curr->next = prv;
		prv = curr;
		curr = next;
	}

	*head = prv;
}

/**
* is_palindrome - func checks if a linked list is a palindrome
* @head: pointer to the pointer of the head of the linked list
*
* Return: 1 if true, 0 if not
*/

int is_palindrome(listint_t **head)
{
	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *temp = *head;
	listint_t *dup = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (1)
	{
		fast = fast->next->next;
		if (!fast)
		{
			dup = slow->next;
			break;
		}
		if (!fast->next)
		{
			dup = slow->next->next;
			break;
		}
		slow = slow->next;
	}

	listint_reversed_(&dup);

	while (dup && temp)
	{
		if (temp->n == dup->n)
		{
			dup = dup->next;
			temp = temp->next;
		}
		else
			return (0);
	}

	if (!dup)
		return (1);
	return (0);
}
