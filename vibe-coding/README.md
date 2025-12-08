
# Vibe Coding Practice

This is a practice folder for coding along with Vibe coding tutorials, specifically Steve Yegge's book on Vibe Coding.

## Projects

This folder contains various JavaScript projects created through AI-assisted prompting. Each project demonstrates different programming concepts and interactive browser-based applications.

### 1. Bouncing Sphere Animation (`bouncing-sphere.html`)
**Prompt:** "Please write a JavaScript app in an artifacts window that animates a bouncing red sphere. Leave a trail behind it. Add gravity and energy when it hits the floor."

**What it does:** 
- Animated red sphere that bounces realistically with physics
- Trail effect that follows the sphere's path with fading opacity
- Gravity simulation that pulls the sphere down
- Energy/bounce physics (85% energy retention on floor impact)
- Wall collision detection on all sides
- Air resistance for realistic motion
- 3D gradient shading with highlights for visual depth

**Technologies:** HTML5 Canvas, vanilla JavaScript, CSS3 gradients

---

### 2. 3D Cube with Dynamic Lighting (`3d-cube-lighting.html`)
**Prompt:** "Write a JavaScript program that shows a cube with a colored light source; create slider bars that can change orientation of the polygon."

**What it does:**
- Interactive 3D cube rendered on HTML5 Canvas
- 6 colored faces (red, green, blue, yellow, magenta, cyan)
- Real-time lighting simulation with diffuse shading
- Visible yellow light source with glow effect
- 6 interactive slider controls:
  - Rotation X, Y, Z axes (rotate the cube)
  - Light Position X, Y, Z (move the light source in 3D space)
- Backface culling for proper depth rendering
- Painter's algorithm for correct face sorting

**Technologies:** 3D mathematics, matrix transformations, lighting calculations, HTML5 Canvas, CSS3

---

### 3. Flappy Bird Game (`flappy-bird.html`)
**Prompt:** "Please create a simple Flappy Bird-like game that I can play in the browser. Make it look nice with some basic styling."

**What it does:**
- Fully playable Flappy Bird clone
- Click or press SPACE to make the bird flap
- Procedurally generated pipe obstacles with random heights
- Score tracking with best score saved to browser localStorage
- Collision detection (pipes, ground, ceiling)
- Smooth animations with rotating bird based on velocity
- Animated clouds in the background
- Game over screen with replay functionality
- Responsive controls and polished visual design

**Technologies:** HTML5 Canvas, game loop with requestAnimationFrame, localStorage, event handling, CSS3 styling


## How to Use

Simply open any `.html` file in a modern web browser (Chrome, Firefox, Safari, Edge) to run the application. No server or build process required - all projects are self-contained single-file applications.

## Learning Outcomes

These projects demonstrate:
- Canvas API and 2D rendering
- Animation techniques using requestAnimationFrame
- Physics simulation (gravity, velocity, collision detection)
- 3D graphics and lighting in 2D canvas
- Matrix transformations and 3D projection
- Game development fundamentals
- User interaction and control systems
- Local storage for data persistence


# Directives for Agents:

1. Run all tests again and report any and all issues
2. Improve your test cases
3. Look for missing edge cases
4. Iterate on version one.
5. 

# Useful Links

https://www.anthropic.com/engineering/claude-code-best-practices



