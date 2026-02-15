# Envelope Animation App – Guide

From the Figma Make export and chat history, here’s how **photo upload** and the **stick-out + slide-out** behavior work (and how to fix them).

---

## 1. How to upload photos so they display

The app has **two places** for images:

### Main 4×6 photo (single “letter photo”)

- **In code:** One image is used for the big photo that peeks out and can be pulled to center.
- **Where to set it (Figma Make / React):**
  - Search for the main photo `<img>` (e.g. `src="https://images.unsplash.com/..."` or "Memory photo").
  - Replace that `src` with your image URL or path.
- **Using your own files:**
  - Put the image in the project’s **`/public`** folder (e.g. `public/photo.jpg`).
  - Set: `src="/photo.jpg"`.
- **Upload at runtime (custom):** Add an `<input type="file" accept="image/*">`, read the file with `FileReader`, set the result (e.g. `reader.result`) as the `src` of that `<img>`. Use one state variable for “main photo URL” and pass it to the image.

### Photo strip (filmstrip images)

- **In code:** An array of filmstrip items, each with `imageUrl` and `alt`.
- **Where to set (Figma Make / React):**
  - Find: `const filmstrips: FilmstripData[] = [ { id: 1, imageUrl: '...', alt: '...' }, ... ]`
  - Replace each `imageUrl` with your image URL or path.
- **Using your own files:**
  - Put images in `/public`, e.g. `filmstrip1.jpg`, `filmstrip2.jpg`, `filmstrip3.jpg`.
  - Use: `imageUrl: '/filmstrip1.jpg'`, etc.
- **Upload at runtime:** Same idea as the main photo: file input → `FileReader` → store data URLs (or upload to a server and store URLs) in state, and set `filmstrips[].imageUrl` from that state.

So: **to have photos “display” in the photo and photo strip**, set the **main photo `src`** and the **filmstrips’ `imageUrl`** (either to static paths/URLs or to URLs/data from your upload flow).

---

## 2. Stick out of the envelope, then slide OUT on click

Desired behavior:

- When the envelope is **open**: the **letter**, the **main photo**, and **one filmstrip** are **sticking out** of the envelope — part visible outside, rest still inside (like real papers in a pocket).
- When you **click** one of them, that item **slides OUT** of the envelope (full slide-out animation) and can be shown in the center or in a designated area.
- Clicking elsewhere (or again) can dock it to the side; clicking the docked item again brings it back to center.

### Layout / structure

- Use a single **envelope “pocket”** (the open rectangle) with a **clipping/mask** so anything inside is only visible above a horizontal “lip” of the envelope.
- **Letter:** Position so the top portion (e.g. 30–40% height) is **above** the envelope lip (sticking out), the rest **inside** the pocket. Same idea for the **photo** and **one filmstrip** — each has a “peek” height (e.g. 40–60px) visible above the lip, rest below (inside).
- **Z-order:** Letter, photo, filmstrip stacked so they don’t overlap badly (e.g. letter on top, then photo, then filmstrip, or vice versa). Use `z-index` and positioning so the “stuck out” parts are visible and clickable.

### Animation: “slides OUT of the envelope”

- **At rest (open envelope):** Each item has:
  - `transform: translateY(0)` (or similar) so the “peek” part is above the lip; the rest is hidden by the envelope mask/overflow.
- **On click (slide out):**
  - Animate that item:
    - `translateY` so the **whole** item moves up and out (e.g. from “partially inside” to “fully above the envelope”).
    - Optionally `scale` and `translate` to move it to center or to a “designated area” on the side.
  - Use CSS `transition` or a library (e.g. Framer Motion / Motion) on `transform` for a smooth slide-out (e.g. 350–450 ms, ease `cubic-bezier(0.4, 0, 0.2, 1)`).
- **After slide-out:** The item is either:
  - **Centered** (large, readable), or
  - **Docked** to the side (smaller, in a fixed area). Clicking the item again can toggle between “docked” and “centered”; clicking backdrop can set it to docked.

### Fixing the “stick out” and “slide out” in code

1. **Envelope pocket with lip**
   - Envelope body = a rectangle. When open, the “inside” is a container with `overflow: hidden` and a top edge that defines the “lip.” Contents (letter, photo, filmstrip) are positioned inside this container so only the top portion (e.g. 30–50px) is visible above the lip.

2. **Initial “stick out” positions**
   - Letter: e.g. `top: 0`, height tall enough that the top part is above the lip (stick out), rest clipped by the envelope.
   - Photo: same idea, offset to the right (or left) so it sticks out on one side.
   - Filmstrip: same, offset so it sticks out on the other side.  
   So all three literally “stick out” of the same envelope opening.

3. **Slide-out on click**
   - On item click: add a class or set state (e.g. `activeItem = 'letter' | 'photo' | 'filmstrip'`).
   - For the active item, apply a `transform` that:
     - Moves it **up** so the whole item is **out** of the envelope (e.g. `translateY(-100%)` or a fixed pixel value so it clears the lip).
     - Then (in the same or a chained animation) move/scale to center or dock position.
   - Other items stay in “stick out” position (or docked if they were previously opened).

4. **Docked vs center**
   - Keep state for “which item is centered” vs “docked.”  
   - Docked = fixed position on left/right, smaller size.  
   - Center = larger, in the middle.  
   - Click item → if docked, animate to center; if centered, animate to dock (or click backdrop → animate to dock).

Implementing the above in the same component that holds the envelope (and the letter/photo/filmstrip elements) will give you the “stick out of the envelope, then slide OUT on click” behavior and a clear place to plug in your uploaded main photo and filmstrip images.
