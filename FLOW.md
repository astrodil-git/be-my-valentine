# Envelope Animation App – Flow (What’s Clicked & What Appears)

## 1. Load / Start

- **On load:** Intro overlay is shown (fullscreen).
- **Visible:** Fullscreen area with **intro video (video2)** and a “Tap to play” overlay.
- **User:** Taps to play → intro video plays.
- **Near end of intro (~1s left):** “Tap to continue” with heart appears.
- **User:** Clicks anywhere on the intro overlay → overlay is dismissed.
- **Result:** Stage becomes visible (envelope and rest of UI). Envelope is **closed**.

---

## 2. Open the Envelope

- **Visible:** Closed envelope (stamp “Open me”, label “For my valentine”), reset heart at bottom (“one more time”).
- **User:** **Clicks the envelope** (envelope-wrap).
- **Result:**
  - Hearts/sparkles animation runs from the envelope.
  - Envelope **opens** (flap up, pocket visible).
  - Inside the pocket: **letter**, **filmstrip**, **photo** (all three visible in the pocket).

---

## 3. Slide Out & Dock Items (Letter, Photo, Filmstrip)

User can open and dock the three items in any order.

### 3a. Slide out an item

- **User:** **Clicks** one of: **letter**, **photo**, or **filmstrip** (in the pocket).
- **Result:**
  - That item **slides out** from the envelope and appears in the middle (or slide-out position).
  - A dim **backdrop** appears behind it.
  - **Letter only:** After ~2s, a **lips icon** appears on the letter (bottom-right).
  - **Photo only:** Cat GIFs may show on the photo (e.g. cat-kiss, peach-cat).

### 3b. Dock the item (put it in its scattered spot)

- **User:** **Clicks the same item again** (or **clicks the backdrop**).
- **Result:**
  - Item **docks** to its fixed position (letter top-left, photo mid-right, filmstrip bottom-left).
  - Backdrop hides.
  - Lips icon hides when the letter is docked.

### 3c. Re-open a docked item (optional)

- **User:** **Clicks** a **docked** item.
- **Result:** That item slides out again (same as 3a). User can then dock it again (3b).

Repeat 3a–3c until **all three** (letter, photo, filmstrip) have been docked at least once.

---

## 4. After All Three Are Docked – “One More Surprise” & End Video

When **letter**, **photo**, and **filmstrip** are all docked:

- **Either:**
  - **User clicks anywhere** on the screen → **“one more surprise…”** overlay appears **immediately**,  
  **or**
  - **No click for 2 seconds** → **“one more surprise…”** overlay appears after 2 seconds.

Then:

- Overlay stays for **3 seconds**, then is removed.
- **End video (video3)** fullscreen overlay appears with **“Tap to play”**.
- **User:** Taps to play → end video plays.
- When the end video is shown, the **two replay video boxes** are revealed: **“Intro”** and **“Our video”** (scattered with the rest of the content).

---

## 5. End State – All Items Scattered (Letter, Filmstrip, Photo, Intro Box, Our Video Box)

- **Visible:**  
  - Open envelope (no more slide-out/dock animations).  
  - **Letter** (top-left), **photo** (mid-right), **filmstrip** (bottom-left).  
  - **Intro** video box (e.g. top, between flap and photo).  
  - **Our video** box (e.g. bottom-right).  
  - **Reset heart** (“one more time”) at bottom center.

- **No further automatic animation.** Only these interactions:

### 5a. Click to center (one at a time)

- **User:** **Clicks** any one of: **letter**, **photo**, **filmstrip**, **Intro** box, or **Our video** box.
- **Result:**
  - That item moves to (or is shown in) the **center** of the screen; a **backdrop** may appear.
  - If another item was already centered, it is **un-centered** first; only the newly clicked item is centered.

### 5b. Click to un-center (“click off”)

- **User:** **Clicks the same centered item again**, or **clicks the backdrop**, or presses **Escape**.
- **Result:** That item returns to its scattered position; nothing is centered.

### 5c. Replay videos (when a video box is “focused” or when clicked)

- **Intro / Our video boxes:**  
  - In versions that support it: clicking the box may **center** it; clicking again may **play** that video in the fullscreen overlay or **un-center** it.  
  - Or: clicking the box once opens the **fullscreen video** (video2 or video3) with “Tap to play.”  
- **Closing the video:** Close button (×), clicking outside the video, or Escape closes the overlay and returns to the scattered view.

### 5d. Restart the entire experience

- **User:** **Clicks the heart** (“one more time”).
- **Result:** **Full reset:**
  - Envelope **closes**.
  - Letter, photo, filmstrip go **back into the pocket**.
  - Surprise overlay and end video overlay are hidden.
  - Replay boxes are hidden.
  - All “centered” state is cleared.
  - Flow effectively returns to **step 2**: user can open the envelope again and go through the whole flow from the beginning.

---

## Summary Table

| Step | What user clicks / does | What appears / happens |
|------|-------------------------|-------------------------|
| Load | (none) | Intro video overlay, “Tap to play” |
| Intro | Tap to play | Intro video plays |
| Intro | Tap to continue (or click overlay) | Overlay dismisses, envelope stage visible, envelope closed |
| Open | Envelope | Envelope opens, hearts/sparkles, letter/photo/filmstrip in pocket |
| Explore | Letter / photo / filmstrip | Item slides out; backdrop; (letter: lips after 2s; photo: cat GIFs) |
| Dock | Same item again or backdrop | Item docks to its scattered position |
| (optional) | Docked item | Item slides out again |
| All docked | Click anywhere **or** wait 2s | “One more surprise…” overlay |
| After surprise | (wait 3s) | Overlay hides, end video (video3) with “Tap to play” |
| End video | Tap to play | End video plays; “Intro” and “Our video” boxes appear |
| End state | Any of 5 items (letter, photo, filmstrip, Intro, Our video) | That item centers (one at a time) |
| End state | Same item again / backdrop / Escape | Item un-centers |
| End state | Heart “one more time” | Full reset; envelope closed; start over from step 2 |

---

## Files

- **index.html** – Static version (may use slightly different end-state behavior, e.g. immediate scatter + click-to-center, no surprise/end-video sequence).
- **templates/envelope.html** – Flask template version with full flow (intro → open → slide/dock → surprise → end video → replay boxes).
- **Reset** is always via the **heart (“one more time”)** only; no other way to restart the full animation.
