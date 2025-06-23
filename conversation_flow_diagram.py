#!/usr/bin/env python3
"""
Conversation Flow Diagrams for AdTech Teaching Assistant
Shows how multi-turn conversations are handled by Strands SDK
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Circle, Arrow
import numpy as np

def create_conversation_flow_diagram():
    """Creates a diagram showing multi-turn conversation handling"""
    fig, ax = plt.subplots(1, 1, figsize=(14, 10))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')
    
    # Colors
    user_blue = '#3B82F6'
    agent_purple = '#6B46C1'
    context_green = '#10B981'
    memory_orange = '#F59E0B'
    
    # Title
    ax.text(7, 9.5, 'Multi-Turn Conversation Flow', fontsize=16, fontweight='bold', ha='center')
    ax.text(7, 9, 'Context-Aware Learning Conversations', fontsize=12, ha='center', style='italic')
    
    # Turn 1
    turn1_y = 8
    user1 = FancyBboxPatch((0.5, turn1_y), 2.5, 0.8, boxstyle="round,pad=0.1", 
                           facecolor=user_blue, edgecolor='black', linewidth=1)
    ax.add_patch(user1)
    ax.text(1.75, turn1_y + 0.4, 'User: "What is RTB?"', fontsize=10, ha='center', color='white')
    
    agent1 = FancyBboxPatch((4, turn1_y), 4, 0.8, boxstyle="round,pad=0.1", 
                            facecolor=agent_purple, edgecolor='black', linewidth=1)
    ax.add_patch(agent1)
    ax.text(6, turn1_y + 0.4, 'Agent: Explains Real-Time Bidding basics', fontsize=10, ha='center', color='white')
    
    context1 = FancyBboxPatch((9, turn1_y), 2.5, 0.8, boxstyle="round,pad=0.1", 
                              facecolor=context_green, edgecolor='black', linewidth=1)
    ax.add_patch(context1)
    ax.text(10.25, turn1_y + 0.4, 'Context: Beginner', fontsize=10, ha='center', color='white')
    
    memory1 = FancyBboxPatch((12, turn1_y), 1.5, 0.8, boxstyle="round,pad=0.1", 
                             facecolor=memory_orange, edgecolor='black', linewidth=1)
    ax.add_patch(memory1)
    ax.text(12.75, turn1_y + 0.4, 'Store: RTB', fontsize=9, ha='center', color='white')
    
    # Turn 2
    turn2_y = 6.5
    user2 = FancyBboxPatch((0.5, turn2_y), 2.5, 0.8, boxstyle="round,pad=0.1", 
                           facecolor=user_blue, edgecolor='black', linewidth=1)
    ax.add_patch(user2)
    ax.text(1.75, turn2_y + 0.4, 'User: "How fast is it?"', fontsize=10, ha='center', color='white')
    
    agent2 = FancyBboxPatch((4, turn2_y), 4, 0.8, boxstyle="round,pad=0.1", 
                            facecolor=agent_purple, edgecolor='black', linewidth=1)
    ax.add_patch(agent2)
    ax.text(6, turn2_y + 0.4, 'Agent: Explains 100ms auction timing', fontsize=10, ha='center', color='white')
    
    context2 = FancyBboxPatch((9, turn2_y), 2.5, 0.8, boxstyle="round,pad=0.1", 
                              facecolor=context_green, edgecolor='black', linewidth=1)
    ax.add_patch(context2)
    ax.text(10.25, turn2_y + 0.4, 'Context: RTB Topic', fontsize=10, ha='center', color='white')
    
    memory2 = FancyBboxPatch((12, turn2_y), 1.5, 0.8, boxstyle="round,pad=0.1", 
                             facecolor=memory_orange, edgecolor='black', linewidth=1)
    ax.add_patch(memory2)
    ax.text(12.75, turn2_y + 0.4, 'Update', fontsize=9, ha='center', color='white')
    
    # Turn 3
    turn3_y = 5
    user3 = FancyBboxPatch((0.5, turn3_y), 2.5, 0.8, boxstyle="round,pad=0.1", 
                           facecolor=user_blue, edgecolor='black', linewidth=1)
    ax.add_patch(user3)
    ax.text(1.75, turn3_y + 0.4, 'User: "What if bid fails?"', fontsize=10, ha='center', color='white')
    
    agent3 = FancyBboxPatch((4, turn3_y), 4, 0.8, boxstyle="round,pad=0.1", 
                            facecolor=agent_purple, edgecolor='black', linewidth=1)
    ax.add_patch(agent3)
    ax.text(6, turn3_y + 0.4, 'Agent: Explains timeout & fallback ads', fontsize=10, ha='center', color='white')
    
    context3 = FancyBboxPatch((9, turn3_y), 2.5, 0.8, boxstyle="round,pad=0.1", 
                              facecolor=context_green, edgecolor='black', linewidth=1)
    ax.add_patch(context3)
    ax.text(10.25, turn3_y + 0.4, 'Context: Advanced', fontsize=10, ha='center', color='white')
    
    memory3 = FancyBboxPatch((12, turn3_y), 1.5, 0.8, boxstyle="round,pad=0.1", 
                             facecolor=memory_orange, edgecolor='black', linewidth=1)
    ax.add_patch(memory3)
    ax.text(12.75, turn3_y + 0.4, 'Mastery+', fontsize=9, ha='center', color='white')
    
    # Context Memory Box
    memory_box = FancyBboxPatch((2, 2.5), 8, 1.5, boxstyle="round,pad=0.1", 
                                facecolor='lightgray', edgecolor='black', linewidth=2)
    ax.add_patch(memory_box)
    ax.text(6, 3.6, 'Strands Agent Context Memory', fontsize=12, fontweight='bold', ha='center')
    ax.text(6, 3.2, '• Conversation History: RTB → Timing → Error Handling', fontsize=10, ha='center')
    ax.text(6, 2.9, '• User Progression: Beginner → Intermediate → Advanced', fontsize=10, ha='center')
    ax.text(6, 2.6, '• Next Suggestions: DSP Integration, Bid Optimization', fontsize=10, ha='center')
    
    # Arrows showing flow
    for y in [turn1_y, turn2_y, turn3_y]:
        ax.arrow(3, y + 0.4, 0.8, 0, head_width=0.1, head_length=0.1, fc='black', ec='black')
        ax.arrow(8, y + 0.4, 0.8, 0, head_width=0.1, head_length=0.1, fc='black', ec='black')
        ax.arrow(11.5, y + 0.4, 0.4, 0, head_width=0.1, head_length=0.1, fc='black', ec='black')
    
    # Memory flow arrows
    for y in [turn1_y, turn2_y, turn3_y]:
        ax.arrow(12.75, y, 0, -0.3, head_width=0.1, head_length=0.1, fc=memory_orange, ec=memory_orange)
    
    # Context awareness arrows
    ax.annotate('', xy=(10.25, turn2_y), xytext=(12.75, turn1_y),
                arrowprops=dict(arrowstyle='->', lw=1.5, color=context_green, 
                               connectionstyle="arc3,rad=0.2"))
    ax.annotate('', xy=(10.25, turn3_y), xytext=(12.75, turn2_y),
                arrowprops=dict(arrowstyle='->', lw=1.5, color=context_green, 
                               connectionstyle="arc3,rad=0.2"))
    
    plt.tight_layout()
    plt.savefig('/Users/keelapud/strands-adtech-teaching-assistant/conversation-flow-diagram.png', 
                dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()

def create_learning_path_diagram():
    """Creates a diagram showing adaptive learning path generation"""
    fig, ax = plt.subplots(1, 1, figsize=(12, 8))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 8)
    ax.axis('off')
    
    # Colors
    beginner_green = '#22C55E'
    intermediate_yellow = '#EAB308'
    advanced_red = '#EF4444'
    expert_purple = '#8B5CF6'
    
    # Title
    ax.text(6, 7.5, 'Adaptive Learning Path Generation', fontsize=16, fontweight='bold', ha='center')
    ax.text(6, 7, 'Personalized Curriculum Based on Progress', fontsize=12, ha='center', style='italic')
    
    # Learning Levels
    levels = [
        (1.5, 5.5, beginner_green, 'Beginner', ['DSP Basics', 'SSP Intro', 'Ad Exchange']),
        (4.5, 5.5, intermediate_yellow, 'Intermediate', ['RTB Process', 'Header Bidding', 'PMPs']),
        (7.5, 5.5, advanced_red, 'Advanced', ['Optimization', 'Attribution', 'Privacy']),
        (10.5, 5.5, expert_purple, 'Expert', ['Custom Algos', 'ML Models', 'Strategy'])
    ]
    
    for x, y, color, level, concepts in levels:
        # Level box
        level_box = FancyBboxPatch((x-0.75, y-1), 1.5, 2, boxstyle="round,pad=0.1", 
                                   facecolor=color, edgecolor='black', linewidth=2)
        ax.add_patch(level_box)
        ax.text(x, y+0.5, level, fontsize=11, fontweight='bold', ha='center', color='white')
        
        # Concepts
        for i, concept in enumerate(concepts):
            ax.text(x, y+0.1-i*0.3, f'• {concept}', fontsize=9, ha='center', color='white')
    
    # Progress arrows
    for i in range(len(levels)-1):
        x1 = levels[i][0] + 0.75
        x2 = levels[i+1][0] - 0.75
        ax.arrow(x1, 5.5, x2-x1, 0, head_width=0.15, head_length=0.2, fc='black', ec='black')
    
    # User Progress Indicator
    progress_box = FancyBboxPatch((2, 3), 8, 1.5, boxstyle="round,pad=0.1", 
                                  facecolor='lightblue', edgecolor='black', linewidth=2)
    ax.add_patch(progress_box)
    ax.text(6, 4, 'Current User: Sarah (Marketing Student)', fontsize=12, fontweight='bold', ha='center')
    ax.text(6, 3.6, 'Progress: Completed Beginner → Starting Intermediate', fontsize=10, ha='center')
    ax.text(6, 3.2, 'Next: RTB Process (adapted for marketing focus)', fontsize=10, ha='center', style='italic')
    
    # Adaptation arrows
    ax.annotate('', xy=(4.5, 4.5), xytext=(6, 4.5),
                arrowprops=dict(arrowstyle='->', lw=2, color='blue'))
    ax.text(5.25, 4.7, 'Adaptive\nPath', fontsize=9, ha='center', color='blue')
    
    # Knowledge Graph
    graph_box = FancyBboxPatch((1, 0.5), 10, 1.5, boxstyle="round,pad=0.1", 
                               facecolor='lightgray', edgecolor='black', linewidth=2)
    ax.add_patch(graph_box)
    ax.text(6, 1.6, 'Strands Agent Knowledge Graph', fontsize=12, fontweight='bold', ha='center')
    ax.text(6, 1.2, 'Concept Dependencies • Learning Prerequisites • Skill Relationships', fontsize=10, ha='center')
    ax.text(6, 0.8, 'Real-time Path Optimization Based on User Performance', fontsize=10, ha='center', style='italic')
    
    plt.tight_layout()
    plt.savefig('/Users/keelapud/strands-adtech-teaching-assistant/learning-path-diagram.png', 
                dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()

if __name__ == "__main__":
    create_conversation_flow_diagram()
    create_learning_path_diagram()
    print("Conversation flow diagrams created successfully!")
