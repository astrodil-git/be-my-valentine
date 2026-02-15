/**
 * Envelope Animation App – layout config
 *
 * Two states:
 *   OPEN   = envelope just opened; letter, filmstrip, photo visible together.
 *   DOCKED = items closed and sitting on the sides with the two video buttons.
 *
 * Edit a value and refresh the page to see the change.
 */

window.ENVELOPE_CONFIG = {
  openState: {
    // The group of 3 items (position/size of the whole block)
    contents: {
      bottom: 51,    // % from pocket bottom (40–75; higher = up)
      height: 85,    // % of pocket height (70–100)
      width: 320,    // px (280–400)
      scale: 0.5,    // 0.3–0.9
    },
    letter:   { rotate: 0, bottom: -9, height: 340 },   // bottom: % from contents bottom; negative = down, positive = up. Or top: % from top.
    filmstrip: { rotate: -30, bottom: 0, height: 320 },
    photo:    { rotate: 35, bottom: 0, height: 260 },
    // Red heart overlay: visible in open state until letter is clicked (then gone for good). On top of everything.
    heart:    { top: 48, left: 49.5, size: 50 },         // top/left: % of stage (50,50 = center). Lower top = higher on screen. size: px.
  },

  dockedState: {
    letter: {
      left: 2, top: 38, marginTop: -160, rotate: -6,
      width: 253, height: 345,
    },
    photo: {
      right: 2, top: 55, marginTop: -120, rotate: 5,
      width: 200, height: 300,
    },
    filmstrip: {
      left: 2, top: 78, marginTop: -60, rotate: -4,
      width: 300, height: 130,
    },
    replayIntro: { left: 65, top: 10, rotate: -6 },   // "Intro" button
    replayEnd:   { right: 18, top: 78, rotate: 10 }, // "Our video" button
  },
};
