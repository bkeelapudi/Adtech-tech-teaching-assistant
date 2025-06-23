#!/usr/bin/env python3
"""
AWS Serverless Architecture Diagram Generator for AdTech Teaching Assistant
Creates a visual representation of the serverless deployment architecture
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, ConnectionPatch
import numpy as np

def create_aws_architecture_diagram():
    fig, ax = plt.subplots(1, 1, figsize=(16, 12))
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 12)
    ax.axis('off')
    
    # Color scheme
    aws_orange = '#FF9900'
    aws_blue = '#232F3E'
    strands_purple = '#6B46C1'
    slack_green = '#4A154B'
    
    # Title
    ax.text(8, 11.5, 'AdTech Teaching Assistant - AWS Serverless Architecture', 
            fontsize=18, fontweight='bold', ha='center')
    ax.text(8, 11, 'Powered by Strands Agents SDK', 
            fontsize=14, ha='center', color=strands_purple, style='italic')
    
    # User Layer
    user_box = FancyBboxPatch((0.5, 9.5), 3, 1.5, 
                              boxstyle="round,pad=0.1", 
                              facecolor='lightblue', 
                              edgecolor='black', linewidth=2)
    ax.add_patch(user_box)
    ax.text(2, 10.2, 'Students & Educators', fontsize=12, fontweight='bold', ha='center')
    ax.text(2, 9.8, 'Slack Workspace', fontsize=10, ha='center', color=slack_green)
    
    # API Gateway
    api_gw_box = FancyBboxPatch((6, 9.5), 3, 1.5, 
                                boxstyle="round,pad=0.1", 
                                facecolor=aws_orange, 
                                edgecolor='black', linewidth=2)
    ax.add_patch(api_gw_box)
    ax.text(7.5, 10.5, 'Amazon API Gateway', fontsize=11, fontweight='bold', ha='center')
    ax.text(7.5, 10.1, 'REST API', fontsize=9, ha='center')
    ax.text(7.5, 9.8, 'WebSocket API', fontsize=9, ha='center')
    
    # CloudFront
    cf_box = FancyBboxPatch((11.5, 9.5), 3, 1.5, 
                            boxstyle="round,pad=0.1", 
                            facecolor=aws_orange, 
                            edgecolor='black', linewidth=2)
    ax.add_patch(cf_box)
    ax.text(13, 10.2, 'Amazon CloudFront', fontsize=11, fontweight='bold', ha='center')
    ax.text(13, 9.8, 'Global CDN', fontsize=9, ha='center')
    
    # Lambda Functions Layer
    lambda_y = 7.5
    
    # Slack Handler Lambda
    slack_lambda = FancyBboxPatch((1, lambda_y), 2.5, 1.2, 
                                  boxstyle="round,pad=0.1", 
                                  facecolor='#FFD700', 
                                  edgecolor='black', linewidth=1)
    ax.add_patch(slack_lambda)
    ax.text(2.25, lambda_y + 0.8, 'AWS Lambda', fontsize=10, fontweight='bold', ha='center')
    ax.text(2.25, lambda_y + 0.5, 'Slack Handler', fontsize=9, ha='center')
    ax.text(2.25, lambda_y + 0.2, 'Event Processing', fontsize=8, ha='center')
    
    # Strands Agent Lambda (Central)
    strands_lambda = FancyBboxPatch((6, lambda_y - 0.3), 4, 1.8, 
                                    boxstyle="round,pad=0.1", 
                                    facecolor=strands_purple, 
                                    edgecolor='black', linewidth=3)
    ax.add_patch(strands_lambda)
    ax.text(8, lambda_y + 1, 'AWS Lambda', fontsize=12, fontweight='bold', ha='center', color='white')
    ax.text(8, lambda_y + 0.7, 'Strands Agents SDK', fontsize=11, fontweight='bold', ha='center', color='white')
    ax.text(8, lambda_y + 0.4, '🧠 NLP Processing', fontsize=9, ha='center', color='white')
    ax.text(8, lambda_y + 0.1, '🎯 Intent Recognition', fontsize=9, ha='center', color='white')
    ax.text(8, lambda_y - 0.2, '📚 Knowledge Integration', fontsize=9, ha='center', color='white')
    
    # Quiz Generator Lambda
    quiz_lambda = FancyBboxPatch((12.5, lambda_y), 2.5, 1.2, 
                                 boxstyle="round,pad=0.1", 
                                 facecolor='#FFD700', 
                                 edgecolor='black', linewidth=1)
    ax.add_patch(quiz_lambda)
    ax.text(13.75, lambda_y + 0.8, 'AWS Lambda', fontsize=10, fontweight='bold', ha='center')
    ax.text(13.75, lambda_y + 0.5, 'Quiz Generator', fontsize=9, ha='center')
    ax.text(13.75, lambda_y + 0.2, 'Assessment Engine', fontsize=8, ha='center')
    
    # Data Layer
    data_y = 5
    
    # DynamoDB
    dynamo_box = FancyBboxPatch((1, data_y), 3, 1.5, 
                                boxstyle="round,pad=0.1", 
                                facecolor='#4B9CD3', 
                                edgecolor='black', linewidth=2)
    ax.add_patch(dynamo_box)
    ax.text(2.5, data_y + 1, 'Amazon DynamoDB', fontsize=11, fontweight='bold', ha='center', color='white')
    ax.text(2.5, data_y + 0.6, 'User Sessions', fontsize=9, ha='center', color='white')
    ax.text(2.5, data_y + 0.3, 'Learning Progress', fontsize=9, ha='center', color='white')
    ax.text(2.5, data_y, 'Quiz Results', fontsize=9, ha='center', color='white')
    
    # S3 Knowledge Base
    s3_box = FancyBboxPatch((6, data_y), 3, 1.5, 
                            boxstyle="round,pad=0.1", 
                            facecolor='#569A31', 
                            edgecolor='black', linewidth=2)
    ax.add_patch(s3_box)
    ax.text(7.5, data_y + 1, 'Amazon S3', fontsize=11, fontweight='bold', ha='center', color='white')
    ax.text(7.5, data_y + 0.6, 'AdTech Knowledge Base', fontsize=9, ha='center', color='white')
    ax.text(7.5, data_y + 0.3, 'Concept Definitions', fontsize=9, ha='center', color='white')
    ax.text(7.5, data_y, 'Learning Materials', fontsize=9, ha='center', color='white')
    
    # ElastiCache
    cache_box = FancyBboxPatch((11.5, data_y), 3, 1.5, 
                               boxstyle="round,pad=0.1", 
                               facecolor='#C925D1', 
                               edgecolor='black', linewidth=2)
    ax.add_patch(cache_box)
    ax.text(13, data_y + 1, 'Amazon ElastiCache', fontsize=11, fontweight='bold', ha='center', color='white')
    ax.text(13, data_y + 0.6, 'Session Cache', fontsize=9, ha='center', color='white')
    ax.text(13, data_y + 0.3, 'Response Cache', fontsize=9, ha='center', color='white')
    ax.text(13, data_y, 'Context Memory', fontsize=9, ha='center', color='white')
    
    # Monitoring & Analytics Layer
    monitor_y = 2.5
    
    # CloudWatch
    cw_box = FancyBboxPatch((2, monitor_y), 3, 1.2, 
                            boxstyle="round,pad=0.1", 
                            facecolor='#FF4B4B', 
                            edgecolor='black', linewidth=2)
    ax.add_patch(cw_box)
    ax.text(3.5, monitor_y + 0.8, 'Amazon CloudWatch', fontsize=10, fontweight='bold', ha='center', color='white')
    ax.text(3.5, monitor_y + 0.5, 'Metrics & Logs', fontsize=9, ha='center', color='white')
    ax.text(3.5, monitor_y + 0.2, 'Performance Monitoring', fontsize=8, ha='center', color='white')
    
    # X-Ray
    xray_box = FancyBboxPatch((6.5, monitor_y), 3, 1.2, 
                              boxstyle="round,pad=0.1", 
                              facecolor='#FF4B4B', 
                              edgecolor='black', linewidth=2)
    ax.add_patch(xray_box)
    ax.text(8, monitor_y + 0.8, 'AWS X-Ray', fontsize=10, fontweight='bold', ha='center', color='white')
    ax.text(8, monitor_y + 0.5, 'Distributed Tracing', fontsize=9, ha='center', color='white')
    ax.text(8, monitor_y + 0.2, 'Performance Analysis', fontsize=8, ha='center', color='white')
    
    # QuickSight
    qs_box = FancyBboxPatch((11, monitor_y), 3, 1.2, 
                            boxstyle="round,pad=0.1", 
                            facecolor='#FF4B4B', 
                            edgecolor='black', linewidth=2)
    ax.add_patch(qs_box)
    ax.text(12.5, monitor_y + 0.8, 'Amazon QuickSight', fontsize=10, fontweight='bold', ha='center', color='white')
    ax.text(12.5, monitor_y + 0.5, 'Learning Analytics', fontsize=9, ha='center', color='white')
    ax.text(12.5, monitor_y + 0.2, 'Usage Dashboards', fontsize=8, ha='center', color='white')
    
    # Security Layer
    security_y = 0.5
    
    # IAM
    iam_box = FancyBboxPatch((3, security_y), 2.5, 1, 
                             boxstyle="round,pad=0.1", 
                             facecolor='#FF9900', 
                             edgecolor='black', linewidth=2)
    ax.add_patch(iam_box)
    ax.text(4.25, security_y + 0.6, 'AWS IAM', fontsize=10, fontweight='bold', ha='center')
    ax.text(4.25, security_y + 0.2, 'Access Control', fontsize=9, ha='center')
    
    # Secrets Manager
    secrets_box = FancyBboxPatch((7, security_y), 2.5, 1, 
                                 boxstyle="round,pad=0.1", 
                                 facecolor='#FF9900', 
                                 edgecolor='black', linewidth=2)
    ax.add_patch(secrets_box)
    ax.text(8.25, security_y + 0.6, 'AWS Secrets Manager', fontsize=10, fontweight='bold', ha='center')
    ax.text(8.25, security_y + 0.2, 'API Keys & Tokens', fontsize=9, ha='center')
    
    # KMS
    kms_box = FancyBboxPatch((10.5, security_y), 2.5, 1, 
                             boxstyle="round,pad=0.1", 
                             facecolor='#FF9900', 
                             edgecolor='black', linewidth=2)
    ax.add_patch(kms_box)
    ax.text(11.75, security_y + 0.6, 'AWS KMS', fontsize=10, fontweight='bold', ha='center')
    ax.text(11.75, security_y + 0.2, 'Encryption', fontsize=9, ha='center')
    
    # Connection arrows
    # User to API Gateway
    ax.arrow(3.5, 10.2, 2.3, 0, head_width=0.1, head_length=0.1, fc='black', ec='black')
    
    # API Gateway to Lambda
    ax.arrow(7.5, 9.5, 0, -1.5, head_width=0.1, head_length=0.1, fc='black', ec='black')
    
    # Slack Lambda to Strands Lambda
    ax.arrow(3.5, 8.1, 2.3, 0, head_width=0.1, head_length=0.1, fc=strands_purple, ec=strands_purple, linewidth=2)
    
    # Strands Lambda to Quiz Lambda
    ax.arrow(10, 8.1, 2.3, 0, head_width=0.1, head_length=0.1, fc=strands_purple, ec=strands_purple, linewidth=2)
    
    # Lambda to Data Layer
    ax.arrow(8, 7.2, 0, -1.5, head_width=0.1, head_length=0.1, fc=strands_purple, ec=strands_purple, linewidth=2)
    
    # Data connections
    ax.arrow(2.5, 6.5, 3.8, 0.3, head_width=0.08, head_length=0.08, fc='gray', ec='gray')
    ax.arrow(9, 6.5, 3.8, -0.3, head_width=0.08, head_length=0.08, fc='gray', ec='gray')
    
    # Add legend
    legend_elements = [
        patches.Patch(color=strands_purple, label='Strands Agents SDK Core'),
        patches.Patch(color=aws_orange, label='AWS Managed Services'),
        patches.Patch(color='#FFD700', label='AWS Lambda Functions'),
        patches.Patch(color='#4B9CD3', label='Database Services'),
        patches.Patch(color='#569A31', label='Storage Services'),
        patches.Patch(color='#FF4B4B', label='Monitoring & Analytics')
    ]
    
    ax.legend(handles=legend_elements, loc='upper right', bbox_to_anchor=(0.98, 0.85))
    
    plt.tight_layout()
    plt.savefig('/Users/keelapud/strands-adtech-teaching-assistant/aws-serverless-architecture.png', 
                dpi=300, bbox_inches='tight', facecolor='white')
    plt.show()

if __name__ == "__main__":
    create_aws_architecture_diagram()
