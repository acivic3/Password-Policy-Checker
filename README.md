# Program Design and Structure

### Inputs

- The user's password to be validated against the policy requirements.

### Constants

- **Minimum length of the password**: 8  
- **Maximum length of the password**: 20  
- The requirement for at least one digit and one alphabetic character.  
- The exclusion of spaces in the password.

### Outputs

Messages indicating whether the password is valid or not, including specific reasons for invalidation, such as:
- Length outside the allowed range.
- Lack of required characters.
- Presence of prohibited characters (e.g., spaces).

---

## Algorithm / Pseudocode

1. Check if the password length is within the specified range (8-20 characters).  
2. Check if the password contains at least one digit and one alphabetic character.  
3. Check if the password does not contain any spaces.  
4. Print a message indicating whether the password is valid. If not valid, provide the specific reason.

---

## Programming Considerations

- The program uses **functions** to modularize different validation checks, improving readability and maintainability.  
- The use of **boolean flags** (`has_digit` and `has_alpha`) in the `contains_required_characters` function to track the presence of required character types.  
- The program provides clear, user-friendly **error messages** to guide users on how to create a compliant password.

---

## Testing Plan

### Test Case 1

- **Inputs**: `UMGC 2024` (contains a space).  
  - Retry with: `UMGC2024`.  
- **Expected Output**:  
  - Error message due to the space in the first input.  
  - Second input (`UMGC2024`) is accepted.

**Purpose**: To test that the program rejects spaces and validates the minimum length of 8 characters.

![Test Case 1](PPC%20-%20Test%20Case%201.png)

---

### Test Case 2

- **Inputs**: `Tw0ThousandTwentyFour` (too long).  
  - Retry with: `20TwentyFour`.  
- **Expected Output**:  
  - Error message due to exceeding the max length in the first input.  
  - Second input (`20TwentyFour`) is accepted.

**Purpose**: To test the maximum password length requirement.

![Test Case 2](PPC%20-%20Test%20Case%202.png)

---

### Test Case 3

- **Inputs**: `UMGCTwentyFour` (no digit).  
  - Retry with: `UMGCTwenty4`.  
- **Expected Output**:  
  - Error message due to the absence of a digit in the first input.  
  - Second input (`UMGCTwenty4`) is accepted.

**Purpose**: To test the digit requirement.

![Test Case 3](PPC%20-%20Test%20Case%203.png)
