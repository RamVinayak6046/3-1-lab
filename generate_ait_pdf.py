import os
import subprocess

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>AIT Lab Manual: Code & Explanations</title>
<style>
  @page {
    size: A4;
    margin: 18mm 15mm 18mm 15mm;
    @bottom-right {
      content: counter(page);
    }
  }

  body {
    font-family: 'Segoe UI', Helvetica, Arial, sans-serif;
    color: #1e293b;
    line-height: 1.55;
    font-size: 11pt;
    margin: 0;
    padding: 0;
  }

  .cover-page {
    page-break-after: always;
    text-align: center;
    padding-top: 80px;
    height: 90vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
  }

  .cover-tag {
    display: inline-block;
    background: #e0e7ff;
    color: #3730a3;
    font-weight: 700;
    padding: 6px 16px;
    border-radius: 20px;
    font-size: 10pt;
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-bottom: 20px;
  }

  .cover-title {
    font-size: 26pt;
    font-weight: 800;
    color: #0f172a;
    margin-bottom: 8px;
    line-height: 1.2;
  }

  .cover-subtitle {
    font-size: 15pt;
    color: #475569;
    font-weight: 600;
    margin-bottom: 40px;
  }

  .cover-card {
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 12px;
    padding: 24px 30px;
    margin: 0 auto 50px auto;
    max-width: 520px;
    text-align: left;
    box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);
  }

  .cover-card div {
    margin-bottom: 8px;
    font-size: 10.5pt;
  }

  .cover-card strong {
    color: #0f172a;
    display: inline-block;
    width: 130px;
  }

  .badge-container {
    margin-top: 30px;
  }

  .badge {
    display: inline-block;
    background: #f1f5f9;
    border: 1px solid #cbd5e1;
    color: #334155;
    padding: 6px 14px;
    border-radius: 6px;
    font-size: 9.5pt;
    font-weight: 600;
    margin: 4px;
  }

  .task-container {
    page-break-before: always;
    padding-top: 10px;
  }

  .task-header {
    border-bottom: 2px solid #2563eb;
    padding-bottom: 8px;
    margin-bottom: 16px;
  }

  .task-num {
    font-size: 10pt;
    font-weight: 700;
    color: #2563eb;
    text-transform: uppercase;
    letter-spacing: 1px;
  }

  .task-title {
    font-size: 18pt;
    font-weight: 800;
    color: #0f172a;
    margin: 4px 0 0 0;
  }

  .section-heading {
    font-size: 12pt;
    font-weight: 700;
    color: #1e3a8a;
    margin-top: 18px;
    margin-bottom: 6px;
    display: flex;
    align-items: center;
    gap: 6px;
  }

  .box-aim {
    background: #eff6ff;
    border-left: 4px solid #2563eb;
    padding: 10px 14px;
    border-radius: 0 8px 8px 0;
    margin-bottom: 14px;
    font-size: 10pt;
  }

  .box-aim strong {
    color: #1d4ed8;
  }

  pre {
    background: #0f172a;
    color: #f8fafc;
    padding: 12px 14px;
    border-radius: 8px;
    font-family: 'Consolas', 'Courier New', monospace;
    font-size: 8.5pt;
    line-height: 1.45;
    overflow-x: auto;
    border: 1px solid #334155;
    margin: 8px 0 16px 0;
    white-space: pre-wrap;
    word-break: break-word;
  }

  .comment { color: #94a3b8; font-style: italic; }
  .keyword { color: #38bdf8; font-weight: bold; }
  .string { color: #a3e635; }
  .func { color: #f472b6; }
  .number { color: #fb923c; }

  .memory-box {
    background: #f0fdf4;
    border: 1px solid #86efac;
    border-left: 4px solid #22c55e;
    padding: 12px 14px;
    border-radius: 0 8px 8px 0;
    margin: 14px 0;
  }

  .memory-box-title {
    font-weight: 800;
    color: #15803d;
    font-size: 10.5pt;
    margin-bottom: 6px;
  }

  .steps-list {
    margin: 6px 0;
    padding-left: 20px;
    font-size: 10pt;
  }

  .steps-list li {
    margin-bottom: 6px;
  }

  .viva-box {
    background: #fefce8;
    border: 1px solid #fde047;
    border-left: 4px solid #eab308;
    padding: 10px 14px;
    border-radius: 0 8px 8px 0;
    margin: 12px 0 20px 0;
    font-size: 9.5pt;
  }

  .viva-title {
    font-weight: 800;
    color: #a16207;
    font-size: 10pt;
    margin-bottom: 4px;
  }

  .highlight-badge {
    background: #fef08a;
    padding: 2px 6px;
    border-radius: 4px;
    font-weight: 600;
    font-size: 9pt;
  }

  table {
    width: 100%;
    border-collapse: collapse;
    margin: 12px 0;
    font-size: 9.5pt;
  }

  th, td {
    border: 1px solid #cbd5e1;
    padding: 7px 10px;
    text-align: left;
  }

  th {
    background: #f1f5f9;
    color: #0f172a;
    font-weight: 700;
  }

  .page-break {
    page-break-before: always;
  }
</style>
</head>
<body>

<!-- COVER PAGE -->
<div class="cover-page">
  <div>
    <span class="cover-tag">Academic Year 2025 – 2026</span>
  </div>
  <div class="cover-title">10212CS211: Artificial Intelligence Techniques</div>
  <div class="cover-subtitle">Lab Tasks Reference & Code Memorization Guide</div>
  
  <div class="cover-card">
    <div><strong>Course Code:</strong> 10212CS211</div>
    <div><strong>Course Title:</strong> Artificial Intelligence Techniques (AIT)</div>
    <div><strong>Department:</strong> Computer Science and Engineering</div>
    <div><strong>Programming Language:</strong> Python 3.x</div>
    <div><strong>Coverage:</strong> Tasks 1 to 10 (Full Manual)</div>
    <div><strong>Content:</strong> Question / Aim, Source Code, Memory Hacks & Logic Breakdown</div>
  </div>

  <div class="badge-container">
    <span class="badge">Graph Search (BFS & DFS)</span>
    <span class="badge">Heuristic Hill Climbing</span>
    <span class="badge">A* Search</span>
    <span class="badge">Minimax Game Tree</span>
    <span class="badge">Ant Colony Optimization (ACO)</span>
    <span class="badge">Constraint Satisfaction</span>
    <span class="badge">Goal Stack Planning</span>
    <span class="badge">N-Queens Backtracking</span>
    <span class="badge">Conversational AI</span>
  </div>
</div>

<!-- TASK 1 -->
<div class="task-container">
  <div class="task-header">
    <div class="task-num">Task 1 (Part A & Part B)</div>
    <div class="task-title">Graph Search Algorithms: BFS & DFS</div>
  </div>

  <div class="box-aim">
    <strong>Aim (Part 1a - Stock Market BFS):</strong> To determine the set of companies impacted within a specified depth (levels of ripple effect) when a given company experiences a significant event, using Breadth-First Search (BFS).<br>
    <strong>Aim (Part 1b - Weather Forecasting DFS):</strong> To traverse a network of weather stations using Depth-First Search (DFS) and display the weather status of each station starting from a designated station.
  </div>

  <div class="section-heading">&#9658; Python Program</div>
  <pre><code><span class="keyword">from</span> collections <span class="keyword">import</span> deque

<span class="comment"># === Part 1a: BFS for Stock Market Influence ===</span>
graph = {
    <span class="string">"Company A"</span>: [<span class="string">"Company B"</span>, <span class="string">"Company C"</span>],
    <span class="string">"Company B"</span>: [<span class="string">"Company D"</span>],
    <span class="string">"Company C"</span>: [<span class="string">"Company D"</span>],
    <span class="string">"Company D"</span>: [<span class="string">"Company E"</span>, <span class="string">"Company F"</span>],
    <span class="string">"Company E"</span>: [], <span class="string">"Company F"</span>: [], <span class="string">"Company G"</span>: []
}

<span class="keyword">def</span> <span class="func">bfs_influence</span>(graph, start_company, max_depth=<span class="number">2</span>):
    queue = deque([[start_company, <span class="number">0</span>]])   <span class="comment"># [node, depth]</span>
    visited = set([start_company])
    impacted = []
    
    <span class="keyword">while</span> queue:
        current, depth = queue.popleft()
        <span class="keyword">if</span> depth == max_depth:
            <span class="keyword">continue</span>
        <span class="keyword">for</span> neighbor <span class="keyword">in</span> graph.get(current, []):
            <span class="keyword">if</span> neighbor <span class="keyword">not in</span> visited:
                visited.add(neighbor)
                impacted.append(neighbor)
                queue.append([neighbor, depth + <span class="number">1</span>])
    <span class="keyword">return</span> impacted

<span class="comment"># === Part 1b: DFS for Weather Stations ===</span>
weather_graph = {
    <span class="string">'station A'</span>: [<span class="string">'station B'</span>, <span class="string">'station C'</span>],
    <span class="string">'station B'</span>: [<span class="string">'station D'</span>],
    <span class="string">'station C'</span>: [<span class="string">'station F'</span>],
    <span class="string">'station D'</span>: [<span class="string">'station E'</span>],
    <span class="string">'station E'</span>: [], <span class="string">'station F'</span>: [], <span class="string">'station P'</span>: []
}
weather_data = {
    <span class="string">'station A'</span>: <span class="string">'sunny'</span>, <span class="string">'station B'</span>: <span class="string">'cloudy'</span>,
    <span class="string">'station C'</span>: <span class="string">'rainy'</span>, <span class="string">'station D'</span>: <span class="string">'stormy'</span>,
    <span class="string">'station E'</span>: <span class="string">'windy'</span>, <span class="string">'station F'</span>: <span class="string">'snowy'</span>
}

<span class="keyword">def</span> <span class="func">dfs</span>(graph, node, visited):
    <span class="keyword">if</span> node <span class="keyword">not in</span> visited:
        print(f<span class="string">"{node} reports: {weather_data[node]}"</span>)
        visited.add(node)
        <span class="keyword">for</span> neighbor <span class="keyword">in</span> graph.get(node, []):
            dfs(graph, neighbor, visited)</code></pre>

  <div class="memory-box">
    <div class="memory-box-title">&#128161; Easy Memory Hook &amp; How to Remember the Code:</div>
    <ul class="steps-list">
      <li><strong>BFS = Queue (FIFO) + Deque:</strong> Remember <em>"BFS spreads like water ripples in all directions"</em>. Store <code>[company, depth]</code> in a queue. Pop left, if <code>depth == max_depth</code> stop expanding that branch, otherwise enqueue neighbors with <code>depth + 1</code>.</li>
      <li><strong>DFS = Recursion (Stack / LIFO):</strong> Remember <em>"DFS goes deep down a rabbit hole first"</em>. Check if not visited &rarr; print weather &rarr; mark visited &rarr; recursively call <code>dfs(graph, neighbor, visited)</code>.</li>
      <li><strong>Data structures:</strong> Always use a <code>set()</code> for <code>visited</code> to prevent infinite cycles in graphs!</li>
    </ul>
  </div>

  <div class="viva-box">
    <div class="viva-title">&#10067; Quick Viva Questions:</div>
    <strong>Q: Why use BFS for stock market impact?</strong><br>
    A: Stock influence cascades level-by-level (direct partners first at depth 1, secondary partners at depth 2). BFS explores by level.<br>
    <strong>Q: What is the time complexity of BFS/DFS?</strong><br>
    A: $O(V + E)$ where $V$ is vertices/companies and $E$ is edges/connections.
  </div>
</div>

<!-- TASK 2 -->
<div class="task-container">
  <div class="task-header">
    <div class="task-num">Task 2</div>
    <div class="task-title">Vehicle Routing using Hill Climbing Algorithm</div>
  </div>

  <div class="box-aim">
    <strong>Aim:</strong> To find an optimized (shortest) route for visiting multiple customers using the Hill Climbing heuristic search algorithm, which iteratively explores neighboring routes and adopts improvements until reaching a local optimum.
  </div>

  <div class="section-heading">&#9658; Python Program</div>
  <pre><code><span class="keyword">import</span> random

<span class="keyword">def</span> <span class="func">generate_random_route</span>(num_customers):
    customers = list(range(<span class="number">1</span>, num_customers + <span class="number">1</span>))
    random.shuffle(customers)
    <span class="keyword">return</span> [<span class="number">0</span>] + customers + [<span class="number">0</span>]  <span class="comment"># Start at depot (0) and return to 0</span>

<span class="keyword">def</span> <span class="func">generate_neighbors</span>(route):
    neighbors = []
    n = len(route)
    <span class="keyword">for</span> i <span class="keyword">in</span> range(<span class="number">1</span>, n - <span class="number">1</span>):
        <span class="keyword">for</span> j <span class="keyword">in</span> range(i + <span class="number">1</span>, n - <span class="number">1</span>):
            neighbor = route.copy()
            neighbor[i], neighbor[j] = neighbor[j], neighbor[i]  <span class="comment"># Swap 2 customers</span>
            neighbors.append(neighbor)
    <span class="keyword">return</span> neighbors

<span class="keyword">def</span> <span class="func">calculate_total_distance</span>(route, dist_matrix):
    <span class="keyword">return</span> sum(dist_matrix[route[i]][route[i+<span class="number">1</span>]] <span class="keyword">for</span> i <span class="keyword">in</span> range(len(route)-<span class="number">1</span>))

<span class="keyword">def</span> <span class="func">hill_climbing</span>(dist_matrix, initial_route):
    current_route = initial_route
    current_distance = calculate_total_distance(current_route, dist_matrix)
    improving = <span class="keyword">True</span>
    
    <span class="keyword">while</span> improving:
        improving = <span class="keyword">False</span>
        neighbors = generate_neighbors(current_route)
        <span class="keyword">for</span> neighbor <span class="keyword">in</span> neighbors:
            neighbor_distance = calculate_total_distance(neighbor, dist_matrix)
            <span class="keyword">if</span> neighbor_distance &lt; current_distance:
                current_route = neighbor
                current_distance = neighbor_distance
                improving = <span class="keyword">True</span>
                <span class="keyword">break</span>  <span class="comment"># First-choice / greedy acceptance</span>
    <span class="keyword">return</span> current_route, current_distance</code></pre>

  <div class="memory-box">
    <div class="memory-box-title">&#128161; Easy Memory Hook &amp; How to Remember the Code:</div>
    <ul class="steps-list">
      <li><strong>4 Key Functions:</strong>
        <ol>
          <li><code>generate_random_route()</code> &rarr; Shuffle numbers 1 to $N$, sandwich between <code>[0] + ... + [0]</code>.</li>
          <li><code>calculate_total_distance()</code> &rarr; Sum edge weights from node $i$ to node $i+1$.</li>
          <li><code>generate_neighbors()</code> &rarr; Nested loops $(i, j)$ swapping two positions inside the route.</li>
          <li><code>hill_climbing()</code> &rarr; <code>while improving:</code> loop. If any neighbor is shorter, accept it and break immediately.</li>
        </ol>
      </li>
      <li><strong>Analogy:</strong> Walking downhill in dense fog. Take a step; if the ground goes lower, move there. Stop when every step in all directions goes up (local minimum).</li>
    </ul>
  </div>

  <div class="viva-box">
    <div class="viva-title">&#10067; Quick Viva Questions:</div>
    <strong>Q: What is the main drawback of standard Hill Climbing?</strong><br>
    A: It can get stuck in a <strong>Local Optimum</strong> (or plateau/ridge) instead of reaching the global optimum.<br>
    <strong>Q: How can local optima be escaped?</strong><br>
    A: Using Random-Restart Hill Climbing, Simulated Annealing, or Genetic Algorithms.
  </div>
</div>

<!-- TASK 3 -->
<div class="task-container">
  <div class="task-header">
    <div class="task-num">Task 3</div>
    <div class="task-title">A* Search Algorithm (Map Navigation)</div>
  </div>

  <div class="box-aim">
    <strong>Aim:</strong> To find the optimal (shortest-cost) path between a start node and goal node in a weighted graph using the A* search algorithm, combining the exact accumulated path cost $g(n)$ and heuristic estimate $h(n)$.
  </div>

  <div class="section-heading">&#9658; Python Program</div>
  <pre><code><span class="keyword">import</span> heapq

graph = {
    <span class="string">'A'</span>: {<span class="string">'B'</span>: <span class="number">6</span>, <span class="string">'F'</span>: <span class="number">3</span>}, <span class="string">'B'</span>: {<span class="string">'C'</span>: <span class="number">1</span>, <span class="string">'G'</span>: <span class="number">6</span>, <span class="string">'F'</span>: <span class="number">3</span>},
    <span class="string">'C'</span>: {<span class="string">'D'</span>: <span class="number">1</span>, <span class="string">'E'</span>: <span class="number">5</span>}, <span class="string">'D'</span>: {<span class="string">'E'</span>: <span class="number">8</span>},
    <span class="string">'E'</span>: {<span class="string">'I'</span>: <span class="number">5</span>, <span class="string">'J'</span>: <span class="number">5</span>}, <span class="string">'F'</span>: {<span class="string">'G'</span>: <span class="number">1</span>, <span class="string">'H'</span>: <span class="number">7</span>},
    <span class="string">'G'</span>: {<span class="string">'H'</span>: <span class="number">3</span>},         <span class="string">'H'</span>: {<span class="string">'I'</span>: <span class="number">2</span>},
    <span class="string">'I'</span>: {<span class="string">'H'</span>: <span class="number">2</span>, <span class="string">'J'</span>: <span class="number">3</span>}, <span class="string">'J'</span>: {}
}

position = {<span class="string">'A'</span>: <span class="number">10</span>, <span class="string">'B'</span>: <span class="number">8</span>, <span class="string">'C'</span>: <span class="number">5</span>, <span class="string">'D'</span>: <span class="number">7</span>, <span class="string">'E'</span>: <span class="number">3</span>, <span class="string">'F'</span>: <span class="number">6</span>, <span class="string">'G'</span>: <span class="number">5</span>, <span class="string">'H'</span>: <span class="number">3</span>, <span class="string">'I'</span>: <span class="number">1</span>, <span class="string">'J'</span>: <span class="number">0</span>}

<span class="keyword">def</span> <span class="func">heuristic</span>(a, b):
    <span class="keyword">return</span> abs(position[a] - position[b])

<span class="keyword">def</span> <span class="func">a_star</span>(graph, start, goal):
    open_set = []
    heapq.heappush(open_set, (heuristic(start, goal), <span class="number">0</span>, start)) <span class="comment"># (f, g, node)</span>
    came_from = {}
    g_score = {node: float(<span class="string">'inf'</span>) <span class="keyword">for</span> node <span class="keyword">in</span> graph}
    g_score[start] = <span class="number">0</span>

    <span class="keyword">while</span> open_set:
        f, g, current = heapq.heappop(open_set)
        <span class="keyword">if</span> current == goal:
            path = []
            <span class="keyword">while</span> current <span class="keyword">in</span> came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            <span class="keyword">return</span> path[::-<span class="number">1</span>], g_score[goal]

        <span class="keyword">for</span> neighbor, cost <span class="keyword">in</span> graph[current].items():
            tentative_g = g_score[current] + cost
            <span class="keyword">if</span> tentative_g &lt; g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score = tentative_g + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f_score, tentative_g, neighbor))
    <span class="keyword">return</span> <span class="keyword">None</span>, float(<span class="string">'inf'</span>)</code></pre>

  <div class="memory-box">
    <div class="memory-box-title">&#128161; Easy Memory Hook &amp; How to Remember the Code:</div>
    <ul class="steps-list">
      <li><strong>The Golden Equation:</strong> <span class="highlight-badge">f(n) = g(n) + h(n)</span>
        <ul>
          <li><code>g(n)</code> = Exact distance travelled from start so far.</li>
          <li><code>h(n)</code> = Heuristic estimated straight-line distance to goal.</li>
          <li><code>f(n)</code> = Total estimated cost &rarr; Always pop the smallest $f$ from the Priority Queue (<code>heapq</code>).</li>
        </ul>
      </li>
      <li><strong>Track Parents with <code>came_from</code>:</strong> To reconstruct the path once you reach the goal, backtrack through <code>came_from</code> dictionary and reverse it: <code>path[::-1]</code>.</li>
    </ul>
  </div>

  <div class="viva-box">
    <div class="viva-title">&#10067; Quick Viva Questions:</div>
    <strong>Q: When is A* guaranteed to find the optimal path?</strong><br>
    A: When the heuristic is <strong>admissible</strong> (it never overestimates the true cost to reach the goal).
  </div>
</div>

<!-- TASK 4 -->
<div class="task-container">
  <div class="task-header">
    <div class="task-num">Task 4</div>
    <div class="task-title">Tic-Tac-Toe using Mini-Max Algorithm</div>
  </div>

  <div class="box-aim">
    <strong>Aim:</strong> To develop an unbeatable Tic-Tac-Toe game where the computer (AI, 'X') plays optimally using the recursive Minimax algorithm, ensuring it either wins or ties against a human player ('O').
  </div>

  <div class="section-heading">&#9658; Python Program</div>
  <pre><code><span class="keyword">import</span> math

<span class="keyword">def</span> <span class="func">check_winner</span>(board):
    wins = [[<span class="number">0</span>,<span class="number">1</span>,<span class="number">2</span>],[<span class="number">3</span>,<span class="number">4</span>,<span class="number">5</span>],[<span class="number">6</span>,<span class="number">7</span>,<span class="number">8</span>],[<span class="number">0</span>,<span class="number">3</span>,<span class="number">6</span>],[<span class="number">1</span>,<span class="number">4</span>,<span class="number">7</span>],[<span class="number">2</span>,<span class="number">5</span>,<span class="number">8</span>],[<span class="number">0</span>,<span class="number">4</span>,<span class="number">8</span>],[<span class="number">2</span>,<span class="number">4</span>,<span class="number">6</span>]]
    <span class="keyword">for</span> line <span class="keyword">in</span> wins:
        <span class="keyword">if</span> board[line[<span class="number">0</span>]] == board[line[<span class="number">1</span>]] == board[line[<span class="number">2</span>]] != <span class="string">' '</span>:
            <span class="keyword">return</span> board[line[<span class="number">0</span>]]
    <span class="keyword">if</span> <span class="string">' '</span> <span class="keyword">not in</span> board: <span class="keyword">return</span> <span class="string">'Tie'</span>
    <span class="keyword">return</span> <span class="keyword">None</span>

<span class="keyword">def</span> <span class="func">minimax</span>(board, is_maximizing):
    winner = check_winner(board)
    <span class="keyword">if</span> winner == <span class="string">'X'</span>: <span class="keyword">return</span> <span class="number">1</span>       <span class="comment"># AI wins</span>
    <span class="keyword">if</span> winner == <span class="string">'O'</span>: <span class="keyword">return</span> -<span class="number">1</span>      <span class="comment"># Human wins</span>
    <span class="keyword">if</span> winner == <span class="string">'Tie'</span>: <span class="keyword">return</span> <span class="number">0</span>

    <span class="keyword">if</span> is_maximizing:  <span class="comment"># AI's turn (maximize score)</span>
        best_score = -math.inf
        <span class="keyword">for</span> i <span class="keyword">in</span> range(<span class="number">9</span>):
            <span class="keyword">if</span> board[i] == <span class="string">' '</span>:
                board[i] = <span class="string">'X'</span>
                score = minimax(board, <span class="keyword">False</span>)
                board[i] = <span class="string">' '</span>        <span class="comment"># Backtrack</span>
                best_score = max(score, best_score)
        <span class="keyword">return</span> best_score
    <span class="keyword">else</span>:              <span class="comment"># Human's turn (minimize score)</span>
        best_score = math.inf
        <span class="keyword">for</span> i <span class="keyword">in</span> range(<span class="number">9</span>):
            <span class="keyword">if</span> board[i] == <span class="string">' '</span>:
                board[i] = <span class="string">'O'</span>
                score = minimax(board, <span class="keyword">True</span>)
                board[i] = <span class="string">' '</span>        <span class="comment"># Backtrack</span>
                best_score = min(score, best_score)
        <span class="keyword">return</span> best_score

<span class="keyword">def</span> <span class="func">best_move</span>(board):
    best_score, move = -math.inf, <span class="keyword">None</span>
    <span class="keyword">for</span> i <span class="keyword">in</span> range(<span class="number">9</span>):
        <span class="keyword">if</span> board[i] == <span class="string">' '</span>:
            board[i] = <span class="string">'X'</span>
            score = minimax(board, <span class="keyword">False</span>)
            board[i] = <span class="string">' '</span>
            <span class="keyword">if</span> score &gt; best_score:
                best_score, move = score, i
    <span class="keyword">return</span> move</code></pre>

  <div class="memory-box">
    <div class="memory-box-title">&#128161; Easy Memory Hook &amp; How to Remember the Code:</div>
    <ul class="steps-list">
      <li><strong>Terminal Values:</strong> AI win = <code>+1</code>, Human win = <code>-1</code>, Draw = <code>0</code>.</li>
      <li><strong>Two Roles:</strong>
        <ul>
          <li><code>is_maximizing == True</code> (AI): Wants highest score &rarr; <code>max(score, best_score)</code>.</li>
          <li><code>is_maximizing == False</code> (Player): Wants lowest score &rarr; <code>min(score, best_score)</code>.</li>
        </ul>
      </li>
      <li><strong>Always Unmake Moves:</strong> Set <code>board[i] = 'X'</code>, call recursion, then immediately reset <code>board[i] = ' '</code> (backtracking).</li>
    </ul>
  </div>

  <div class="viva-box">
    <div class="viva-title">&#10067; Quick Viva Questions:</div>
    <strong>Q: How can Minimax be optimized?</strong><br>
    A: By implementing <strong>Alpha-Beta Pruning</strong> to avoid exploring branches that cannot influence the final decision.
  </div>
</div>

<!-- TASK 5 -->
<div class="task-container">
  <div class="task-header">
    <div class="task-num">Task 5</div>
    <div class="task-title">Ant Colony Optimization (ACO) for Route Optimization</div>
  </div>

  <div class="box-aim">
    <strong>Aim:</strong> To find the shortest delivery route that visits all given cities once and returns to the starting depot using Ant Colony Optimization (ACO) inspired by the foraging behavior of real ants.
  </div>

  <div class="section-heading">&#9658; Python Program</div>
  <pre><code><span class="keyword">import</span> numpy <span class="keyword">as</span> np
<span class="keyword">import</span> random

cities = [<span class="string">"Depot"</span>, <span class="string">"Mumbai"</span>, <span class="string">"Delhi"</span>, <span class="string">"Chennai"</span>, <span class="string">"Kolkata"</span>, 
          <span class="string">"Bangalore"</span>, <span class="string">"Hyderabad"</span>, <span class="string">"Pune"</span>, <span class="string">"Ahmedabad"</span>, <span class="string">"Jaipur"</span>, <span class="string">"Lucknow"</span>]
<span class="comment"># dist_matrix is an 11x11 numpy array of distances</span>

n_locations, n_ants, n_iterations = len(cities), <span class="number">20</span>, <span class="number">100</span>
alpha, beta, rho, Q = <span class="number">1.0</span>, <span class="number">5.0</span>, <span class="number">0.5</span>, <span class="number">100</span>
pheromone = np.ones((n_locations, n_locations))

<span class="keyword">def</span> <span class="func">ant_tour</span>():
    tour = [<span class="number">0</span>]
    unvisited = list(range(<span class="number">1</span>, n_locations))
    <span class="keyword">while</span> unvisited:
        i = tour[-1]
        probs = []
        <span class="keyword">for</span> j <span class="keyword">in</span> unvisited:
            tau = pheromone[i, j] ** alpha            <span class="comment"># Pheromone factor</span>
            eta = (<span class="number">1.0</span> / dist_matrix[i, j]) ** beta   <span class="comment"># Heuristic visibility (1/distance)</span>
            probs.append(tau * eta)
        probs = np.array(probs) / np.sum(probs)      <span class="comment"># Normalize probabilities</span>
        next_city = random.choices(unvisited, weights=probs, k=<span class="number">1</span>)[<span class="number">0</span>]
        tour.append(next_city)
        unvisited.remove(next_city)
    tour.append(<span class="number">0</span>)  <span class="comment"># Return to depot</span>
    <span class="keyword">return</span> tour

<span class="comment"># ACO Simulation Loop</span>
best_route, best_length = <span class="keyword">None</span>, float(<span class="string">"inf"</span>)
<span class="keyword">for</span> _ <span class="keyword">in</span> range(n_iterations):
    routes, lengths = [], []
    <span class="keyword">for</span> _ <span class="keyword">in</span> range(n_ants):
        t = ant_tour()
        L = sum(dist_matrix[t[k], t[k+<span class="number">1</span>]] <span class="keyword">for</span> k <span class="keyword">in</span> range(len(t)-<span class="number">1</span>))
        routes.append(t); lengths.append(L)
        <span class="keyword">if</span> L &lt; best_length: best_length, best_route = L, t
    
    pheromone *= (<span class="number">1</span> - rho)  <span class="comment"># Evaporation</span>
    <span class="keyword">for</span> r, L <span class="keyword">in</span> zip(routes, lengths):
        <span class="keyword">for</span> k <span class="keyword">in</span> range(len(r)-<span class="number">1</span>):
            pheromone[r[k], r[k+<span class="number">1</span>]] += Q / L  <span class="comment"># Deposit pheromone</span></code></pre>

  <div class="memory-box">
    <div class="memory-box-title">&#128161; Easy Memory Hook &amp; How to Remember the Code:</div>
    <ul class="steps-list">
      <li><strong>The Core Probability Rule:</strong> $P_{ij} \propto (\tau_{ij})^\alpha \times (\eta_{ij})^\beta$
        <ul>
          <li>$\tau$ (tau) = Pheromone (history of where other ants succeeded).</li>
          <li>$\eta$ (eta) = Visibility ($1 / \text{distance}$) &rarr; Closer cities have higher attraction.</li>
        </ul>
      </li>
      <li><strong>Two Essential Updates:</strong>
        <ol>
          <li><code>pheromone *= (1 - rho)</code> &rarr; Evaporation (old trails fade away).</li>
          <li><code>pheromone += Q / length</code> &rarr; Deposit (shorter routes get MORE pheromone).</li>
        </ol>
      </li>
    </ul>
  </div>

  <div class="viva-box">
    <div class="viva-title">&#10067; Quick Viva Questions:</div>
    <strong>Q: What happens if evaporation rate ($\rho$) is 0?</strong><br>
    A: Pheromone accumulates indefinitely without fading, leading to premature convergence on bad paths.
  </div>
</div>

<!-- TASK 6 -->
<div class="task-container">
  <div class="task-header">
    <div class="task-num">Task 6</div>
    <div class="task-title">Map Coloring using Constraint Satisfaction (CSP)</div>
  </div>

  <div class="box-aim">
    <strong>Aim:</strong> To assign the minimum possible colors (frequencies/signals) to adjacent zones in a graph such that no two neighboring zones share the same color, using a Greedy Graph Coloring algorithm.
  </div>

  <div class="section-heading">&#9658; Python Program</div>
  <pre><code><span class="keyword">from</span> collections <span class="keyword">import</span> defaultdict

<span class="keyword">class</span> <span class="func">Graph</span>:
    <span class="keyword">def</span> <span class="func">__init__</span>(self, vertices):
        self.v = vertices
        self.graph = defaultdict(list)

    <span class="keyword">def</span> <span class="func">add_edge</span>(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    <span class="keyword">def</span> <span class="func">greedy_coloring</span>(self, max_colors=<span class="keyword">None</span>):
        result = [-<span class="number">1</span>] * self.v       <span class="comment"># -1 indicates uncolored</span>
        available = [<span class="keyword">True</span>] * self.v  <span class="comment"># available[c] = True means color c is free</span>

        <span class="keyword">for</span> u <span class="keyword">in</span> range(self.v):
            <span class="comment"># 1. Mark neighbor colors as unavailable</span>
            <span class="keyword">for</span> neighbor <span class="keyword">in</span> self.graph[u]:
                <span class="keyword">if</span> result[neighbor] != -<span class="number">1</span>:
                    available[result[neighbor]] = <span class="keyword">False</span>

            <span class="comment"># 2. Pick the lowest available color</span>
            color = <span class="number">0</span>
            <span class="keyword">while</span> color &lt; self.v:
                <span class="keyword">if</span> available[color]: <span class="keyword">break</span>
                color += <span class="number">1</span>
            result[u] = color

            <span class="comment"># 3. Reset available array for next vertex</span>
            <span class="keyword">for</span> neighbor <span class="keyword">in</span> self.graph[u]:
                <span class="keyword">if</span> result[neighbor] != -<span class="number">1</span>:
                    available[result[neighbor]] = <span class="keyword">True</span>

        max_used = max(result) + <span class="number">1</span>
        <span class="keyword">if</span> max_colors <span class="keyword">is not None</span>:
            <span class="keyword">if</span> max_used &lt;= max_colors:
                print(f<span class="string">" With {max_colors} colors: Coloring is possible!"</span>)
            <span class="keyword">else</span>:
                print(f<span class="string">" With {max_colors} colors: Coloring is NOT possible!"</span>)
        <span class="keyword">return</span> result</code></pre>

  <div class="memory-box">
    <div class="memory-box-title">&#128161; Easy Memory Hook &amp; How to Remember the Code:</div>
    <ul class="steps-list">
      <li><strong>Remember the 3-Step Dance:</strong>
        <ol>
          <li>Look at neighbors: Mark their colors as <code>False</code> in <code>available</code>.</li>
          <li>Find lowest color index that is still <code>True</code> &rarr; Assign to current node.</li>
          <li>Reset neighbor colors back to <code>True</code> for the next node!</li>
        </ol>
      </li>
      <li><strong>Variables to Remember:</strong> <code>result = [-1]*V</code> (stores assigned color), <code>available = [True]*V</code> (scratchpad).</li>
    </ul>
  </div>

  <div class="viva-box">
    <div class="viva-title">&#10067; Quick Viva Questions:</div>
    <strong>Q: What is the Chromatic Number of a graph?</strong><br>
    A: The minimum number of colors needed to color the graph such that no two adjacent vertices have the same color.
  </div>
</div>

<!-- TASK 7 -->
<div class="task-container">
  <div class="task-header">
    <div class="task-num">Task 7</div>
    <div class="task-title">Monkey Banana Problem in Goal Stack Planning</div>
  </div>

  <div class="box-aim">
    <strong>Aim:</strong> To simulate a robot performing goal-oriented actions (moving to location, climbing a ladder, and retrieving a tool from a shelf) using state transitions and goal stack verification in Python.
  </div>

  <div class="section-heading">&#9658; Python Program</div>
  <pre><code><span class="comment"># Initial states</span>
robot_location = <span class="string">"A"</span>
ladder_location = <span class="string">"B"</span>
tool_location = <span class="string">"C"</span>
robot_has_tool = <span class="keyword">False</span>
robot_on_ladder = <span class="keyword">False</span>

print(<span class="string">"Robot starting at"</span>, robot_location)

<span class="comment"># Step 1: Move to ladder</span>
robot_location = ladder_location
print(<span class="string">"Robot picked up the ladder"</span>)
print(<span class="string">"Robot moved to tool location"</span>, robot_location)
robot_on_ladder = <span class="keyword">True</span>

<span class="comment"># Step 2: Robot climbs and picks tool</span>
print(<span class="string">"Robot placed ladder and climbed up"</span>)
robot_has_tool = <span class="keyword">True</span>
print(<span class="string">"Robot picked tool from shelf"</span>)
robot_on_ladder = <span class="keyword">False</span>

<span class="comment"># Step 3: Climb down and goal check</span>
print(<span class="string">"Robot climbed down safely"</span>)
print(<span class="string">"In Goal state Reached:"</span>)
print(<span class="string">"Robot has tool:"</span>, robot_has_tool)</code></pre>

  <div class="memory-box">
    <div class="memory-box-title">&#128161; Easy Memory Hook &amp; How to Remember the Code:</div>
    <ul class="steps-list">
      <li><strong>5 State Variables:</strong> 3 positions (<code>A, B, C</code>) and 2 booleans (<code>has_tool=False</code>, <code>on_ladder=False</code>).</li>
      <li><strong>3 Action Sequences (STRIPS operators):</strong>
        <ol>
          <li><code>MOVE(A &rarr; B)</code> and drag ladder to tool.</li>
          <li><code>CLIMB(ladder)</code> and <code>GRASP(tool)</code> &rarr; <code>has_tool = True</code>.</li>
          <li><code>DESCEND(ladder)</code> &rarr; <code>on_ladder = False</code> &rarr; Check goal!</li>
        </ol>
      </li>
    </ul>
  </div>

  <div class="viva-box">
    <div class="viva-title">&#10067; Quick Viva Questions:</div>
    <strong>Q: What is Goal Stack Planning?</strong><br>
    A: A classical AI planning algorithm that uses a stack of subgoals and STRIPS operators (Preconditions, Add-list, Delete-list) to reach a desired target state.
  </div>
</div>

<!-- TASK 8 -->
<div class="task-container">
  <div class="task-header">
    <div class="task-num">Task 8</div>
    <div class="task-title">N-Queens Problem using Backtracking</div>
  </div>

  <div class="box-aim">
    <strong>Aim:</strong> To place $N$ non-attacking queens on an $N \times N$ chessboard such that no two queens share the same row, column, or diagonal, using recursive backtracking.
  </div>

  <div class="section-heading">&#9658; Python Program</div>
  <pre><code><span class="keyword">def</span> <span class="func">solve_n_queens</span>(n=<span class="number">4</span>):
    solutions = []
    cols = set()       <span class="comment"># Track attacked columns</span>
    diag1 = set()      <span class="comment"># Track positive diagonals: (r + c)</span>
    diag2 = set()      <span class="comment"># Track negative diagonals: (r - c)</span>
    board = [-<span class="number">1</span>] * n

    <span class="keyword">def</span> <span class="func">backtrack</span>(r=<span class="number">0</span>):
        <span class="keyword">if</span> r == n:
            solutions.append(board.copy())
            <span class="keyword">return</span>
        <span class="keyword">for</span> c <span class="keyword">in</span> range(n):
            <span class="keyword">if</span> c <span class="keyword">in</span> cols <span class="keyword">or</span> (r + c) <span class="keyword">in</span> diag1 <span class="keyword">or</span> (r - c) <span class="keyword">in</span> diag2:
                <span class="keyword">continue</span>   <span class="comment"># Conflict detected!</span>

            <span class="comment"># Place Queen</span>
            cols.add(c); diag1.add(r + c); diag2.add(r - c)
            board[r] = c
            
            backtrack(r + <span class="number">1</span>)  <span class="comment"># Recurse to next row</span>

            <span class="comment"># Backtrack: Remove Queen</span>
            cols.remove(c); diag1.remove(r + c); diag2.remove(r - c)
            board[r] = -<span class="number">1</span>

    backtrack(<span class="number">0</span>)
    <span class="keyword">return</span> solutions

<span class="keyword">def</span> <span class="func">format_solutions</span>(sol):
    n = len(sol[<span class="number">0</span>])
    res = []
    <span class="keyword">for</span> s <span class="keyword">in</span> sol:
        grid = [<span class="string">'.'</span> * n <span class="keyword">for</span> _ <span class="keyword">in</span> range(n)]
        <span class="keyword">for</span> r <span class="keyword">in</span> range(n):
            row = list(grid[r]); row[s[r]] = <span class="string">'Q'</span>; grid[r] = <span class="string">''</span>.join(row)
        res.append(<span class="string">'\\n'</span>.join(grid))
    <span class="keyword">return</span> <span class="string">'\\n\\n'</span>.join(res)</code></pre>

  <div class="memory-box">
    <div class="memory-box-title">&#128161; Easy Memory Hook &amp; How to Remember the Code:</div>
    <ul class="steps-list">
      <li><strong>The 3 Sets Trick (No nested safety check loops needed!):</strong>
        <ol>
          <li><code>cols.add(c)</code> &rarr; Checks column conflict.</li>
          <li><code>diag1.add(r + c)</code> &rarr; Checks $/$-diagonal (sum $r+c$ is constant).</li>
          <li><code>diag2.add(r - c)</code> &rarr; Checks $\backslash$-diagonal (difference $r-c$ is constant).</li>
        </ol>
      </li>
      <li><strong>Always clean up:</strong> Add before recursing, <code>.remove()</code> immediately after recursion returns!</li>
    </ul>
  </div>

  <div class="viva-box">
    <div class="viva-title">&#10067; Quick Viva Questions:</div>
    <strong>Q: How many solutions exist for 4-Queens?</strong><br>
    A: Exactly 2 distinct solutions (reflection of each other). For 8-Queens, there are 92 solutions.
  </div>
</div>

<!-- TASK 9 -->
<div class="task-container">
  <div class="task-header">
    <div class="task-num">Task 9</div>
    <div class="task-title">Intelligent Chatbot System using Conversational AI</div>
  </div>

  <div class="box-aim">
    <strong>Aim:</strong> To build an intelligent chatbot system using Python and OpenAI/NLP principles to demonstrate semantic intent analysis, context preservation, and conversational response generation.
  </div>

  <div class="section-heading">&#9658; Python Program</div>
  <pre><code><span class="comment"># Simple ChatGPT & Assistant System</span>
<span class="keyword">def</span> <span class="func">run_simple_chatgpt</span>():
    print(<span class="string">"--- 9a: Simple ChatGPT using OpenAI ---"</span>)
    query = <span class="string">"Give me 3 ideas that i could build using openai apis"</span>
    print(f<span class="string">"User Query: {query}\\n"</span>)
    
    ideas = (
        <span class="string">"1. Personalized Content Recommendation System: AI suggestions based on user history.\\n"</span>
        <span class="string">"2. Intelligent Chatbot: Automated customer queries and transaction completions.\\n"</span>
        <span class="string">"3. Fraud Detection System: Identifies fraudulent transactions using anomaly classification."</span>
    )
    print(<span class="string">"Output:\\n"</span>, ideas)

<span class="keyword">def</span> <span class="func">run_chatgpt_assistant</span>():
    print(<span class="string">"\\n--- 9b: ChatGPT Assistant using OpenAI ---"</span>)
    system_msg = <span class="string">"Nila's personal chatbot"</span>
    print(f<span class="string">"What type of chatbot would you like to create?\\n{system_msg}"</span>)
    print(<span class="string">"Your new assistant is ready! Type your query"</span>)
    print(<span class="string">"User: Hello! How can you assist me today?"</span>)
    print(<span class="string">"Assistant: Hello Nila! I am your personal AI assistant. I can help organize tasks."</span>)

<span class="keyword">if</span> __name__ == <span class="string">"__main__"</span>:
    run_simple_chatgpt()
    run_chatgpt_assistant()</code></pre>

  <div class="memory-box">
    <div class="memory-box-title">&#128161; Easy Memory Hook &amp; How to Remember the Code:</div>
    <ul class="steps-list">
      <li><strong>Chat Roles Architecture:</strong>
        <ul>
          <li><code>system</code>: Defines persona and personality of the bot.</li>
          <li><code>user</code>: User query message.</li>
          <li><code>assistant</code>: Model-generated reply appended to conversation history.</li>
        </ul>
      </li>
      <li><strong>3 Applications to mention:</strong> Recommendation Engine, Customer Support Bot, Fraud Anomaly Detector.</li>
    </ul>
  </div>

  <div class="viva-box">
    <div class="viva-title">&#10067; Quick Viva Questions:</div>
    <strong>Q: What is the purpose of Dialogflow / NLP in chatbots?</strong><br>
    A: It parses unstructured user text into structured <strong>Intents</strong> (what user wants) and <strong>Entities</strong> (parameters/data).
  </div>
</div>

<!-- TASK 10 -->
<div class="task-container">
  <div class="task-header">
    <div class="task-num">Task 10</div>
    <div class="task-title">Simple Fact Verification Engine in Python</div>
  </div>

  <div class="box-aim">
    <strong>Aim:</strong> To implement a knowledge-base fact verification system in Python that parses statement strings and validates their truth value against known conditional rules.
  </div>

  <div class="section-heading">&#9658; Python Program</div>
  <pre><code><span class="comment"># Define a list of facts</span>
facts = [
    <span class="string">"john_is_cold."</span>,              <span class="comment"># john is cold</span>
    <span class="string">"raining."</span>,                   <span class="comment"># it is raining</span>
    <span class="string">"john_Forgot_His_Raincoat."</span>,  <span class="comment"># john forgot his raincoat</span>
    <span class="string">"fred_lost_his_car_keys."</span>,    <span class="comment"># fred lost his car keys</span>
    <span class="string">"peter_footballer."</span>           <span class="comment"># peter plays football</span>
]

<span class="keyword">def</span> <span class="func">verify_fact</span>(fact):
    fact = fact.rstrip(<span class="string">"."</span>)       <span class="comment"># Strip trailing punctuation</span>
    
    <span class="comment"># Knowledge Base Rules</span>
    <span class="keyword">if</span> fact == <span class="string">"john_Forgot_His_Raincoat"</span>:
        <span class="keyword">return</span> <span class="keyword">True</span>
    <span class="keyword">elif</span> fact == <span class="string">"raining"</span>:
        <span class="keyword">return</span> <span class="keyword">True</span>
    <span class="keyword">elif</span> fact == <span class="string">"foggy"</span>:
        <span class="keyword">return</span> <span class="keyword">True</span>
    <span class="keyword">elif</span> fact == <span class="string">"Cloudy"</span>:
        <span class="keyword">return</span> <span class="keyword">False</span>
    <span class="keyword">else</span>:
        <span class="keyword">return</span> <span class="keyword">False</span>

<span class="keyword">if</span> __name__ == <span class="string">"__main__"</span>:
    <span class="keyword">for</span> fact <span class="keyword">in</span> facts:
        <span class="keyword">if</span> verify_fact(fact):
            print(f<span class="string">"{fact} - Yes"</span>)
        <span class="keyword">else</span>:
            print(f<span class="string">"{fact} - No"</span>)</code></pre>

  <div class="memory-box">
    <div class="memory-box-title">&#128161; Easy Memory Hook &amp; How to Remember the Code:</div>
    <ul class="steps-list">
      <li><strong>Crucial Step:</strong> Always strip the trailing dot with <code>fact.rstrip(".")</code> before matching strings!</li>
      <li><strong>Rules:</strong> Only <code>"john_Forgot_His_Raincoat"</code> and <code>"raining"</code> return <code>True</code> (&rarr; <code>Yes</code>). All other facts return <code>False</code> (&rarr; <code>No</code>).</li>
    </ul>
  </div>

  <div class="viva-box">
    <div class="viva-title">&#10067; Quick Viva Questions:</div>
    <strong>Q: What AI concept does this represent?</strong><br>
    A: <strong>Rule-based Expert Systems</strong> and propositional logic knowledge representation.
  </div>
</div>

</body>
</html>
"""

html_path = os.path.join(os.environ["TEMP"], "ait_guide.html")
with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"HTML generated at {html_path}")
