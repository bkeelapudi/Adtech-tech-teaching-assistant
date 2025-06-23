#!/usr/bin/env python3
"""
Technical Workflow Diagrams for AdTech Teaching Assistant
Creates visual representations of key system workflows
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Rectangle, Circle
import numpy as np

def create_concept_explanation_workflow():
    """Creates workflow diagram for concept explanation process"""
    fig, ax = plt.subplots(1, 1, figsize=(14, 10))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')
    
    # Colors
    strands_purple = '#6B46C1'
    process_blue = '#3B82F6'
    data_green = '#10B981'
    output_orange = '#F59E0B'
    
    # Title
    ax.text(7, 9.5, 'Concept Explanation Workflow', fontsize=16, fontweight='bold', ha='center')
    ax.text(7, 9, 'How Strands Agents SDK Processes Learning Requests', fontsize=12, ha='center', style='italic')
    
    # Step 1: User Input
    step1 = FancyBboxPatch((0.5, 7.5), 2.5, 1, boxstyle="round,pad=0.1", 
                           facecolor='lightblue', edgecolor='black', linewidth=2)
    ax.add_patch(step1)
    ax.text(1.75, 8, 'User Query', fontsize=11, fontweight='bold', ha='center')
    ax.text(1.75, 7.7, '"What is a DSP?"', fontsize=9, ha='center', style='italic')
    
    # Step 2: Slack Handler
    step2 = FancyBboxPatch((4, 7.5), 2.5, 1, boxstyle="round,pad=0.1", 
                           facecolor=process_blue, edgecolor='black', linewidth=2)
    ax.add_patch(step2)
    ax.text(5.25, 8, 'Slack Handler', fontsize=11, fontweight='bold', ha='center', color='white')
    ax.text(5.25, 7.7, 'Event Processing', fontsize=9, ha='center', color='white')
    
    # Step 3: Strands Agent Core
    step3 = FancyBboxPatch((7.5, 6.5), 3, 2, boxstyle="round,pad=0.1", 
                           facecolor=strands_purple, edgecolor='black', linewidth=3)
    ax.add_patch(step3)
    ax.text(9, 7.8, 'Strands Agent SDK', fontsize=12, fontweight='bold', ha='center', color='white')
    ax.text(9, 7.5, '🧠 NLP Processing', fontsize=10, ha='center', color='white')
    ax.text(9, 7.2, '🎯 Intent Recognition', fontsize=10, ha='center', color='white')
    ax.text(9, 6.9, '📊 Context Analysis', fontsize=10, ha='center', color='white')
    ax.text(9, 6.6, '🔍 User Profiling', fontsize=10, ha='center', color='white')
    
    # Step 4: Knowledge Base Query
    step4 = FancyBboxPatch((11.5, 7.5), 2, 1, boxstyle="round,pad=0.1", 
                           facecolor=data_green, edgecolor='black', linewidth=2)
    ax.add_patch(step4)
    ax.text(12.5, 8, 'Knowledge Base', fontsize=11, fontweight='bold', ha='center', color='white')
    ax.text(12.5, 7.7, 'Concept Retrieval', fontsize=9, ha='center', color='white')
    
    # Step 5: Context Processing
    step5 = FancyBboxPatch((2, 5), 3, 1.5, boxstyle="round,pad=0.1", 
                           facecolor=strands_purple, edgecolor='black', linewidth=2)
    ax.add_patch(step5)
    ax.text(3.5, 5.9, 'Context Processing', fontsize=11, fontweight='bold', ha='center', color='white')
    ax.text(3.5, 5.6, '• User Learning Level', fontsize=9, ha='center', color='white')
    ax.text(3.5, 5.3, '• Previous Concepts', fontsize=9, ha='center', color='white')
    ax.text(3.5, 5.0, '• Conversation History', fontsize=9, ha='center', color='white')
    
    # Step 6: Response Generation
    step6 = FancyBboxPatch((6, 5), 3, 1.5, boxstyle="round,pad=0.1", 
                           facecolor=strands_purple, edgecolor='black', linewidth=2)
    ax.add_patch(step6)
    ax.text(7.5, 5.9, 'Response Generation', fontsize=11, fontweight='bold', ha='center', color='white')
    ax.text(7.5, 5.6, '• Adaptive Explanation', fontsize=9, ha='center', color='white')
    ax.text(7.5, 5.3, '• Related Concepts', fontsize=9, ha='center', color='white')
    ax.text(7.5, 5.0, '• Follow-up Suggestions', fontsize=9, ha='center', color='white')
    
    # Step 7: Response Formatting
    step7 = FancyBboxPatch((10, 5), 3, 1.5, boxstyle="round,pad=0.1", 
                           facecolor=output_orange, edgecolor='black', linewidth=2)
    ax.add_patch(step7)
    ax.text(11.5, 5.9, 'Response Formatting', fontsize=11, fontweight='bold', ha='center', color='white')
    ax.text(11.5, 5.6, '• Slack Blocks', fontsize=9, ha='center', color='white')
    ax.text(11.5, 5.3, '• Interactive Elements', fontsize=9, ha='center', color='white')
    ax.text(11.5, 5.0, '• Rich Media', fontsize=9, ha='center', color='white')
    
    # Step 8: User Response
    step8 = FancyBboxPatch((5.5, 2.5), 3, 1.5, boxstyle="round,pad=0.1", 
                           facecolor='lightgreen', edgecolor='black', linewidth=2)
    ax.add_patch(step8)
    ax.text(7, 3.4, 'Formatted Response', fontsize=11, fontweight='bold', ha='center')
    ax.text(7, 3.1, '🏗️ DSP Explanation', fontsize=9, ha='center')
    ax.text(7, 2.8, '📚 Related: SSP, RTB', fontsize=9, ha='center')
    ax.text(7, 2.5, '❓ Quiz Available', fontsize=9, ha='center')
    
    # Step 9: Learning State Update
    step9 = FancyBboxPatch((10, 2.5), 2.5, 1.5, boxstyle="round,pad=0.1", 
                           facecolor=data_green, edgecolor='black', linewidth=2)
    ax.add_patch(step9)
    ax.text(11.25, 3.4, 'State Update', fontsize=11, fontweight='bold', ha='center', color='white')
    ax.text(11.25, 3.1, 'Progress Tracking', fontsize=9, ha='center', color='white')
    ax.text(11.25, 2.8, 'Session Memory', fontsize=9, ha='center', color='white')
    
    # Arrows
    arrows = [
        (3, 8, 0.8, 0),      # 1 to 2
        (6.5, 8, 0.8, 0),    # 2 to 3
        (10.5, 7.8, 0.8, 0), # 3 to 4
        (9, 6.5, -5.5, -1),  # 3 to 5
        (5, 5.75, 0.8, 0),   # 5 to 6
        (9, 5.75, 0.8, 0),   # 6 to 7
        (11.5, 5, -4, -2),   # 7 to 8
        (8.5, 3.25, 1.3, 0), # 8 to 9
    ]
    
    for x, y, dx, dy in arrows:
        ax.arrow(x, y, dx, dy, head_width=0.1, head_length=0.1, fc='black', ec='black')
    
    # Add feedback loop
    ax.annotate('', xy=(9, 6.5), xytext=(11.25, 2.5),
                arrowprops=dict(arrowstyle='->', lw=1.5, color='red', 
                               connectionstyle="arc3,rad=0.3"))
    ax.text(12, 4.5, 'Feedback Loop', fontsize=9, color='red', rotation=-45)
    
    plt.tight_layout()
    plt.savefig('/Users/keelapud/strands-adtech-teaching-assistant/concept-explanation-workflow.png', 
                dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()

def create_quiz_generation_workflow():
    """Creates workflow diagram for quiz generation process"""
    fig, ax = plt.subplots(1, 1, figsize=(12, 8))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 8)
    ax.axis('off')
    
    # Colors
    strands_purple = '#6B46C1'
    quiz_yellow = '#EAB308'
    assessment_red = '#EF4444'
    
    # Title
    ax.text(6, 7.5, 'Adaptive Quiz Generation Workflow', fontsize=16, fontweight='bold', ha='center')
    ax.text(6, 7, 'Personalized Assessment Creation', fontsize=12, ha='center', style='italic')
    
    # User Profile Analysis
    profile_box = FancyBboxPatch((0.5, 5.5), 2.5, 1.5, boxstyle="round,pad=0.1", 
                                 facecolor=strands_purple, edgecolor='black', linewidth=2)
    ax.add_patch(profile_box)
    ax.text(1.75, 6.5, 'User Profile', fontsize=11, fontweight='bold', ha='center', color='white')
    ax.text(1.75, 6.2, 'Analysis', fontsize=11, fontweight='bold', ha='center', color='white')
    ax.text(1.75, 5.9, '• Learning Progress', fontsize=9, ha='center', color='white')
    ax.text(1.75, 5.6, '• Weak Areas', fontsize=9, ha='center', color='white')
    
    # Knowledge Gap Detection
    gap_box = FancyBboxPatch((4.5, 5.5), 2.5, 1.5, boxstyle="round,pad=0.1", 
                             facecolor=assessment_red, edgecolor='black', linewidth=2)
    ax.add_patch(gap_box)
    ax.text(5.75, 6.5, 'Knowledge Gap', fontsize=11, fontweight='bold', ha='center', color='white')
    ax.text(5.75, 6.2, 'Detection', fontsize=11, fontweight='bold', ha='center', color='white')
    ax.text(5.75, 5.9, '• Concept Mastery', fontsize=9, ha='center', color='white')
    ax.text(5.75, 5.6, '• Difficulty Mapping', fontsize=9, ha='center', color='white')
    
    # Question Generation
    question_box = FancyBboxPatch((8.5, 5.5), 2.5, 1.5, boxstyle="round,pad=0.1", 
                                  facecolor=quiz_yellow, edgecolor='black', linewidth=2)
    ax.add_patch(question_box)
    ax.text(9.75, 6.5, 'Question', fontsize=11, fontweight='bold', ha='center')
    ax.text(9.75, 6.2, 'Generation', fontsize=11, fontweight='bold', ha='center')
    ax.text(9.75, 5.9, '• Targeted Topics', fontsize=9, ha='center')
    ax.text(9.75, 5.6, '• Adaptive Difficulty', fontsize=9, ha='center')
    
    # Quiz Assembly
    assembly_box = FancyBboxPatch((2, 3.5), 3, 1.5, boxstyle="round,pad=0.1", 
                                  facecolor=strands_purple, edgecolor='black', linewidth=2)
    ax.add_patch(assembly_box)
    ax.text(3.5, 4.5, 'Quiz Assembly', fontsize=11, fontweight='bold', ha='center', color='white')
    ax.text(3.5, 4.2, '• Question Sequencing', fontsize=9, ha='center', color='white')
    ax.text(3.5, 3.9, '• Difficulty Progression', fontsize=9, ha='center', color='white')
    ax.text(3.5, 3.6, '• Interactive Format', fontsize=9, ha='center', color='white')
    
    # Real-time Adaptation
    adapt_box = FancyBboxPatch((7, 3.5), 3, 1.5, boxstyle="round,pad=0.1", 
                               facecolor=assessment_red, edgecolor='black', linewidth=2)
    ax.add_patch(adapt_box)
    ax.text(8.5, 4.5, 'Real-time Adaptation', fontsize=11, fontweight='bold', ha='center', color='white')
    ax.text(8.5, 4.2, '• Answer Analysis', fontsize=9, ha='center', color='white')
    ax.text(8.5, 3.9, '• Difficulty Adjustment', fontsize=9, ha='center', color='white')
    ax.text(8.5, 3.6, '• Follow-up Questions', fontsize=9, ha='center', color='white')
    
    # Performance Analytics
    analytics_box = FancyBboxPatch((4.5, 1.5), 3, 1.5, boxstyle="round,pad=0.1", 
                                   facecolor=quiz_yellow, edgecolor='black', linewidth=2)
    ax.add_patch(analytics_box)
    ax.text(6, 2.5, 'Performance Analytics', fontsize=11, fontweight='bold', ha='center')
    ax.text(6, 2.2, '• Score Calculation', fontsize=9, ha='center')
    ax.text(6, 1.9, '• Learning Recommendations', fontsize=9, ha='center')
    ax.text(6, 1.6, '• Progress Update', fontsize=9, ha='center')
    
    # Arrows
    ax.arrow(3, 6.25, 1.3, 0, head_width=0.1, head_length=0.1, fc='black', ec='black')
    ax.arrow(7, 6.25, 1.3, 0, head_width=0.1, head_length=0.1, fc='black', ec='black')
    ax.arrow(5.75, 5.5, -2.5, -1.5, head_width=0.1, head_length=0.1, fc='black', ec='black')
    ax.arrow(9.75, 5.5, -2.5, -1.5, head_width=0.1, head_length=0.1, fc='black', ec='black')
    ax.arrow(5, 4.25, 1.8, 0, head_width=0.1, head_length=0.1, fc='black', ec='black')
    ax.arrow(8.5, 3.5, -2, -1.5, head_width=0.1, head_length=0.1, fc='black', ec='black')
    
    # Feedback loop
    ax.annotate('', xy=(1.75, 5.5), xytext=(6, 1.5),
                arrowprops=dict(arrowstyle='->', lw=1.5, color='red', 
                               connectionstyle="arc3,rad=-0.3"))
    ax.text(0.5, 3.5, 'Learning\nFeedback', fontsize=9, color='red', ha='center')
    
    plt.tight_layout()
    plt.savefig('/Users/keelapud/strands-adtech-teaching-assistant/quiz-generation-workflow.png', 
                dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()

if __name__ == "__main__":
    create_concept_explanation_workflow()
    create_quiz_generation_workflow()
    print("Workflow diagrams created successfully!")
